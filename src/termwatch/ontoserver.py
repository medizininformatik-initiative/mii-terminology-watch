"""Minimal FHIR terminology-server client (stdlib only).

Configuration via environment:
  TERMWATCH_FHIR_BASE   base URL, default https://ontoserver.mii-termserv.de/fhir
  TERMWATCH_CERT        client certificate (PEM) for mTLS, optional
  TERMWATCH_KEY         private key (PEM), optional
  TERMWATCH_KEY_PASS    passphrase for the key, optional
"""
from __future__ import annotations

import json
import os
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterable, List, Optional, Tuple

SCT = "http://snomed.info/sct"
LOINC = "http://loinc.org"
SCT_INT_MODULE = "900000000000207008"

# SNOMED historical association refsets exposed by Ontoserver as implicit ConceptMaps
HISTORICAL_ASSOCIATIONS = {
    "900000000000526001": "REPLACED BY",
    "900000000000527005": "SAME AS",
    "900000000000523009": "POSSIBLY EQUIVALENT TO",
    "1186924009": "PARTIALLY EQUIVALENT TO",
    "900000000000530003": "ALTERNATIVE",
    "900000000000528000": "WAS A",
    "900000000000525002": "MOVED TO",
}


def sct_version_uri(edition_module: str, date: str) -> str:
    return f"{SCT}/{edition_module}/version/{date}"


class TerminologyServer:
    def __init__(self, base: Optional[str] = None, retries: int = 3) -> None:
        self.base = (base or os.environ.get("TERMWATCH_FHIR_BASE", "https://ontoserver.mii-termserv.de/fhir")).rstrip("/")
        self.retries = retries
        self._ctx: Optional[ssl.SSLContext] = None
        self.calls = 0

    def _context(self) -> ssl.SSLContext:
        if self._ctx is None:
            ctx = ssl.create_default_context()
            cert = os.environ.get("TERMWATCH_CERT")
            if cert:
                ctx.load_cert_chain(cert, os.environ.get("TERMWATCH_KEY") or None, password=os.environ.get("TERMWATCH_KEY_PASS") or None)
            self._ctx = ctx
        return self._ctx

    def call(self, path: str, params: Optional[Iterable[Tuple[str, str]]] = None, body: Optional[dict] = None, timeout: int = 180) -> dict:
        url = self.base + path + (("?" + urllib.parse.urlencode(list(params))) if params else "")
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method="POST" if data else "GET",
                                     headers={"Accept": "application/fhir+json", "Content-Type": "application/fhir+json"})
        last: dict = {}
        for attempt in range(self.retries):
            self.calls += 1
            try:
                with urllib.request.urlopen(req, context=self._context(), timeout=timeout) as r:
                    return json.loads(r.read())
            except urllib.error.HTTPError as e:
                try:
                    last = json.loads(e.read())
                except Exception:
                    last = {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "diagnostics": f"HTTP {e.code}"}]}
                if e.code < 500:
                    return last
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                last = {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "diagnostics": str(e)}]}
            time.sleep(2 * (attempt + 1))
        return last

    # ---- CodeSystem versions -------------------------------------------------
    def code_system_versions(self, system: str) -> List[str]:
        b = self.call("/CodeSystem", [("url", system), ("_elements", "version"), ("_count", "200")])
        return sorted(e["resource"].get("version", "") for e in b.get("entry", []))

    # ---- $expand -------------------------------------------------------------
    def expand(self, valueset: dict, force_versions: Dict[str, str], page: int = 50000, max_total: int = 500000,
               properties: Iterable[str] = ("inactive",), soft_versions: Optional[Dict[str, str]] = None) -> Tuple[Dict[str, dict], dict]:
        """Expand an inline ValueSet under code-system versions.

        force_versions override every include (also pinned ones); soft_versions
        (FHIR system-version) only apply to includes without a version, which is
        what a ValueSet that unions several pinned yearly releases needs.

        Returns (contains, info) where contains maps code -> {display, inactive, system}
        and info holds total / truncated / error.
        """
        contains: Dict[str, dict] = {}
        offset = 0
        info: dict = {"total": None, "truncated": False, "error": None}
        while True:
            pars: List[dict] = [
                {"name": "valueSet", "resource": valueset},
                {"name": "count", "valueInteger": page},
                {"name": "offset", "valueInteger": offset},
                {"name": "activeOnly", "valueBoolean": False},
                {"name": "includeDesignations", "valueBoolean": False},
            ]
            pars += [{"name": "property", "valueString": p} for p in properties]
            pars += [{"name": "force-system-version", "valueCanonical": f"{sys_}|{ver}"} for sys_, ver in force_versions.items()]
            pars += [{"name": "system-version", "valueCanonical": f"{sys_}|{ver}"} for sys_, ver in (soft_versions or {}).items()]
            r = self.call("/ValueSet/$expand", body={"resourceType": "Parameters", "parameter": pars})
            if r.get("resourceType") != "ValueSet":
                info["error"] = "; ".join(i.get("diagnostics") or i.get("details", {}).get("text", "") for i in r.get("issue", []))[:500] or "unknown error"
                return contains, info
            ex = r.get("expansion", {})
            info["total"] = ex.get("total")
            for c in ex.get("contains", []):
                contains[f"{c['system']}|{c['code']}"] = {"system": c["system"], "code": c["code"], "display": c.get("display", ""),
                                                           "inactive": bool(c.get("inactive", False))}
            offset += page
            if info["total"] is None or offset >= info["total"]:
                return contains, info
            if offset >= max_total:
                info["truncated"] = True
                return contains, info

    # ---- $validate-code ------------------------------------------------------
    def validate(self, system: str, code: str, version: str) -> dict:
        r = self.call("/CodeSystem/$validate-code", [("url", system), ("code", code), ("version", version)])
        out = {p["name"]: next((v for k, v in p.items() if k.startswith("value")), None) for p in r.get("parameter", [])}
        return {"result": out.get("result"), "inactive": out.get("inactive"), "display": out.get("display"), "message": out.get("message")}

    # ---- $lookup -------------------------------------------------------------
    def lookup(self, system: str, code: str, version: str, properties: Iterable[str] = ("inactive",)) -> dict:
        pars = [("system", system), ("code", code), ("version", version)] + [("property", p) for p in properties]
        r = self.call("/CodeSystem/$lookup", pars)
        props: Dict[str, Any] = {}
        for p in r.get("parameter", []):
            if p.get("name") == "property" and len(p.get("part", [])) > 1:
                k = p["part"][0].get("valueCode")
                v = next((v for kk, v in p["part"][1].items() if kk.startswith("value")), None)
                props.setdefault(k, []).append(v)
        display = next((p.get("valueString") for p in r.get("parameter", []) if p.get("name") == "display"), None)
        return {"display": display, "properties": props, "found": r.get("resourceType") == "Parameters"}

    # ---- SNOMED successors ---------------------------------------------------
    def sct_successors(self, code: str, version: str) -> List[dict]:
        out: List[dict] = []
        for refset, name in HISTORICAL_ASSOCIATIONS.items():
            t = self.call("/ConceptMap/$translate", [("url", f"{SCT}?fhir_cm={refset}"), ("system", SCT), ("code", code), ("version", version)])
            for m in (p for p in t.get("parameter", []) if p.get("name") == "match"):
                coding = next((pp.get("valueCoding") for pp in m.get("part", []) if pp.get("name") == "concept"), None)
                if coding:
                    out.append({"association": name, "code": coding.get("code"), "display": coding.get("display", "")})
        return out
