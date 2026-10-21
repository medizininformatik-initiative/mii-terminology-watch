"""Local SNOMED CT backend over RF2 release archives (stdlib only).

The MII Ontoserver lags the SNOMED International release train by a few months.
An RF2 archive (zip or extracted directory, Snapshot files) can stand in for the
server for one SNOMED CT version: it answers the same four questions compare.py
asks — expand a ValueSet, is a code active, what is its display, which concepts
replace an inactive one — with the same return shapes as TerminologyServer.

Supported includes: enumerated concepts; filters concept is-a / descendent-of;
constraint = ECL limited to <, <<, >, >>, AND/OR/MINUS, brackets and concept
references. Refined ECL (": attribute = ...") raises, like an invalid ECL does.
Filters return active concepts only (matches Ontoserver's ECL expansion), enumerated
concepts are returned with inactive=true when inactive and dropped when unknown.

Parsed snapshots are cached as a pickle under $TERMWATCH_CACHE (default ~/.cache/termwatch),
so the first use of a release takes a few minutes and later ones a few seconds.
"""
from __future__ import annotations

import io
import os
import pickle
import re
import sys
import time
import zipfile
from collections import deque
from typing import Dict, Iterable, Iterator, List, Optional, Set, Tuple

from .ontoserver import HISTORICAL_ASSOCIATIONS, SCT, TerminologyServer

IS_A = "116680003"
SYNONYM = "900000000000013009"
FSN = "900000000000003001"
PREFERRED = "900000000000548007"
LANG_REFSETS_PREFERRED = ("900000000000509007", "900000000000508004", "31000274107")  # en-US, en-GB, de (Germany edition)
INACTIVATION_REFSET = "900000000000489007"
INACTIVATION_REASONS = {
    "900000000000482003": "Duplicate", "900000000000483008": "Outdated", "900000000000484002": "Ambiguous",
    "900000000000485001": "Erroneous", "900000000000486000": "Limited", "900000000000487009": "Moved elsewhere",
    "900000000000492006": "Pending move", "1186917008": "Classification derived", "1186919006": "Nonconformance to editorial policy",
    "723277005": "Nonconformance to editorial policy", "1186918003": "Meaning unknown", "723278000": "Not semantically equivalent",
}
EDITIONS = [  # archive-name marker -> edition module (the version URI's middle part)
    ("InternationalRF2", "900000000000207008"), ("Germany", "11000274103"),
    ("ManagedServiceAT", "11000234105"), ("ManagedServiceCH", "2011000195101"),
]
CACHE_FORMAT = 2


def _edition_and_date(name: str) -> Tuple[str, str]:
    m = re.search(r"_(\d{8})T\d{6}Z", name)
    if not m:
        raise ValueError(f"cannot read the release date from archive name {name!r}; use PATH=VERSION_URI")
    module = next((mod for marker, mod in EDITIONS if marker in name), None)
    if not module:
        raise ValueError(f"unknown edition in archive name {name!r}; use PATH=VERSION_URI")
    return module, m.group(1)


class Rf2Release:
    """One SNOMED CT release read from an RF2 Snapshot (zip archive or directory)."""

    def __init__(self, path: str, version: Optional[str] = None, cache_dir: Optional[str] = None, quiet: bool = False) -> None:
        self.path = os.path.expanduser(path)
        if not os.path.exists(self.path):
            raise FileNotFoundError(self.path)
        name = os.path.basename(self.path.rstrip("/"))
        if version:
            self.version = version
        else:
            module, date = _edition_and_date(name)
            self.version = f"{SCT}/{module}/version/{date}"
        self.base = f"rf2:{name}"
        self.calls = 0
        self.quiet = quiet
        self.cache_dir = cache_dir or os.environ.get("TERMWATCH_CACHE") or os.path.expanduser("~/.cache/termwatch")
        self._cache_file = os.path.join(self.cache_dir, re.sub(r"\.zip$", "", name) + ".pickle")
        self.active: Set[str] = set()
        self.known: Set[str] = set()
        self.children: Dict[str, List[str]] = {}
        self.pt: Dict[str, str] = {}
        self.assoc: Dict[str, List[Tuple[str, str]]] = {}
        self.inactivation: Dict[str, str] = {}
        self._load()

    # ---- reading ------------------------------------------------------------
    def _members(self) -> List[str]:
        if zipfile.is_zipfile(self.path):
            with zipfile.ZipFile(self.path) as z:
                return z.namelist()
        out = []
        for root, _, files in os.walk(self.path):
            out += [os.path.join(root, f) for f in files]
        return out

    def _rows(self, pattern: str) -> Iterator[List[str]]:
        rx = re.compile(pattern)
        names = [n for n in self._members() if "/Snapshot/" in n and rx.search(os.path.basename(n))]
        if not names:
            raise FileNotFoundError(f"no Snapshot file matching {pattern} in {self.path}")
        for name in names:
            if zipfile.is_zipfile(self.path):
                z = zipfile.ZipFile(self.path)
                fh = io.TextIOWrapper(z.open(name), encoding="utf-8", newline="")
            else:
                fh = open(name, encoding="utf-8", newline="")
            with fh:
                next(fh)  # header
                for line in fh:
                    yield line.rstrip("\r\n").split("\t")

    def _log(self, msg: str) -> None:
        if not self.quiet:
            print(f"[rf2 {self.version.rsplit('/', 1)[-1]}] {msg}", file=sys.stderr, flush=True)

    def _load(self) -> None:
        if os.path.exists(self._cache_file):
            with open(self._cache_file, "rb") as f:
                d = pickle.load(f)
            if d.get("format") == CACHE_FORMAT and d.get("version") == self.version:
                self.active, self.known, self.children = d["active"], d["known"], d["children"]
                self.pt, self.assoc, self.inactivation = d["pt"], d["assoc"], d["inactivation"]
                return
        t0 = time.time()
        self._log("parsing concepts")
        for r in self._rows(r"^sct2_Concept_Snapshot"):
            self.known.add(r[0])
            if r[2] == "1":
                self.active.add(r[0])
        self._log(f"{len(self.known)} concepts ({len(self.active)} active); parsing is-a relationships")
        for r in self._rows(r"^sct2_Relationship_Snapshot"):
            # id effectiveTime active moduleId sourceId destinationId relationshipGroup typeId ...
            if r[2] == "1" and r[7] == IS_A:
                self.children.setdefault(r[5], []).append(r[4])
        self._log(f"{sum(len(v) for v in self.children.values())} is-a edges; parsing descriptions")
        synonyms: Dict[str, Tuple[str, str]] = {}
        for r in self._rows(r"^sct2_Description_Snapshot"):
            # id effectiveTime active moduleId conceptId languageCode typeId term caseSignificanceId
            if r[2] == "1" and r[6] == SYNONYM:
                synonyms[r[0]] = (r[4], r[7])
        self._log(f"{len(synonyms)} active synonyms; parsing language refsets")
        rank = {rs: i for i, rs in enumerate(LANG_REFSETS_PREFERRED)}
        best: Dict[str, int] = {}
        for r in self._rows(r"^der2_cRefset_Language"):
            # id effectiveTime active moduleId refsetId referencedComponentId acceptabilityId
            if r[2] == "1" and r[6] == PREFERRED and r[4] in rank and r[5] in synonyms:
                cid, term = synonyms[r[5]]
                if rank[r[4]] < best.get(cid, 99):
                    best[cid] = rank[r[4]]
                    self.pt[cid] = term
        del synonyms
        self._log(f"{len(self.pt)} preferred terms; parsing historical associations")
        for r in self._rows(r"^der2_cRefset_Association"):
            # id effectiveTime active moduleId refsetId referencedComponentId targetComponentId
            if r[2] == "1" and r[4] in HISTORICAL_ASSOCIATIONS:
                self.assoc.setdefault(r[5], []).append((r[4], r[6]))
        for r in self._rows(r"^der2_cRefset_AttributeValue"):
            # id effectiveTime active moduleId refsetId referencedComponentId valueId
            if r[2] == "1" and r[4] == INACTIVATION_REFSET and r[5] in self.known:
                self.inactivation[r[5]] = r[6]
        self._log(f"parsed in {time.time() - t0:.0f}s; caching to {self._cache_file}")
        os.makedirs(self.cache_dir, exist_ok=True)
        with open(self._cache_file, "wb") as f:
            pickle.dump({"format": CACHE_FORMAT, "version": self.version, "active": self.active, "known": self.known,
                         "children": self.children, "pt": self.pt, "assoc": self.assoc, "inactivation": self.inactivation}, f,
                        protocol=pickle.HIGHEST_PROTOCOL)

    # ---- hierarchy / ECL -------------------------------------------------------
    def descendants(self, code: str, include_self: bool = False) -> Set[str]:
        out: Set[str] = set()
        if include_self and code in self.active:
            out.add(code)
        q = deque(self.children.get(code, ()))
        while q:
            c = q.popleft()
            if c in out or c not in self.active:
                continue
            out.add(c)
            q.extend(self.children.get(c, ()))
        return out

    def ancestors(self, code: str, include_self: bool = False) -> Set[str]:
        if not hasattr(self, "_parents"):
            self._parents: Dict[str, List[str]] = {}
            for p, cs in self.children.items():
                for c in cs:
                    self._parents.setdefault(c, []).append(p)
        out: Set[str] = set()
        if include_self and code in self.active:
            out.add(code)
        q = deque(self._parents.get(code, ()))
        while q:
            c = q.popleft()
            if c in out or c not in self.active:
                continue
            out.add(c)
            q.extend(self._parents.get(c, ()))
        return out

    _TOK = re.compile(r"\s*(<<|<|>>|>|\(|\)|AND|OR|MINUS|\d{6,18})\s*(?:\|[^|]*\|)?\s*", re.I)

    def ecl(self, expr: str) -> Set[str]:
        """Minimal ECL: < << > >> concept, AND / OR / MINUS, brackets. Anything else raises ValueError."""
        tokens: List[str] = []
        pos = 0
        while pos < len(expr):
            m = self._TOK.match(expr, pos)
            if not m:
                raise ValueError(f"unsupported ECL near {expr[pos:pos + 30]!r}")
            tokens.append(m.group(1).upper() if m.group(1).isalpha() else m.group(1))
            pos = m.end()
        tokens.append(None)
        i = [0]

        def peek():
            return tokens[i[0]]

        def take():
            t = tokens[i[0]]; i[0] += 1; return t

        def atom() -> Set[str]:
            t = take()
            if t == "(":
                s = expression()
                if take() != ")":
                    raise ValueError("unbalanced brackets in ECL")
                return s
            if t in ("<", "<<", ">", ">>"):
                c = take()
                if not (c and c.isdigit()):
                    raise ValueError(f"expected a concept after {t!r} in ECL")
                if t.startswith("<"):
                    return self.descendants(c, include_self=t == "<<")
                return self.ancestors(c, include_self=t == ">>")
            if t and t.isdigit():
                return {t} if t in self.active else set()
            raise ValueError(f"unexpected token {t!r} in ECL")

        def expression() -> Set[str]:
            s = atom()
            while peek() in ("AND", "OR", "MINUS"):
                op = take()
                r = atom()
                s = s & r if op == "AND" else s | r if op == "OR" else s - r
            return s

        s = expression()
        if peek() is not None:
            raise ValueError(f"unexpected token {peek()!r} in ECL (refinements are not supported)")
        return s

    # ---- TerminologyServer interface ----------------------------------------------
    def code_system_versions(self, system: str) -> List[str]:
        return [self.version] if system == SCT else []

    def _include(self, inc: dict) -> Set[str]:
        if inc.get("valueSet"):
            raise ValueError("valueSet references cannot be resolved from an RF2 archive")
        if inc.get("concept"):
            return {c["code"] for c in inc["concept"] if c["code"] in self.known}
        if inc.get("filter"):
            sets = []
            for f in inc["filter"]:
                prop, op, val = f.get("property"), f.get("op"), (f.get("value") or "").strip()
                if prop in ("concept", "code") and op == "is-a":
                    # Ontoserver keeps the anchor itself even when it is inactive (flagged inactive=true)
                    sets.append(self.descendants(val) | ({val} if val in self.known else set()))
                elif prop in ("concept", "code") and op == "descendent-of":
                    sets.append(self.descendants(val))
                elif prop == "constraint" and op == "=":
                    sets.append(self.ecl(val))
                elif prop in ("concept", "code") and op == "in":
                    sets.append({c.strip() for c in val.split(",") if c.strip() in self.known})
                else:
                    raise ValueError(f"unsupported filter {prop} {op}")
            return set.intersection(*sets) if sets else set()
        return set(self.active)  # whole system

    def expand(self, valueset: dict, force_versions: Dict[str, str], page: int = 50000, max_total: int = 500000,
               properties: Iterable[str] = ("inactive",), soft_versions: Optional[Dict[str, str]] = None) -> Tuple[Dict[str, dict], dict]:
        self.calls += 1
        info: dict = {"total": None, "truncated": False, "error": None}
        comp = valueset.get("compose", {})
        foreign = {i.get("system") for i in comp.get("include", []) + comp.get("exclude", [])} - {SCT}
        if foreign:
            info["error"] = f"RF2 backend only expands SNOMED CT includes, got {sorted(foreign)}"
            return {}, info
        wanted = (force_versions or {}).get(SCT) or (soft_versions or {}).get(SCT)
        if wanted and wanted != self.version:
            info["error"] = f"RF2 archive holds {self.version}, not {wanted}"
            return {}, info
        try:
            codes: Set[str] = set()
            for inc in comp.get("include", []):
                if inc.get("version") and inc["version"] != self.version and SCT not in (force_versions or {}):
                    info["error"] = f"include pinned to {inc['version']}, archive holds {self.version}"
                    return {}, info
                codes |= self._include(inc)
            for exc in comp.get("exclude", []):
                codes -= self._include(exc)
        except ValueError as e:
            info["error"] = str(e)
            return {}, info
        info["total"] = len(codes)
        if len(codes) > max_total:
            info["truncated"] = True
            codes = set(sorted(codes)[:max_total])
        contains = {f"{SCT}|{c}": {"system": SCT, "code": c, "display": self.pt.get(c, ""), "inactive": c not in self.active} for c in codes}
        return contains, info

    def validate(self, system: str, code: str, version: str) -> dict:
        self.calls += 1
        if system != SCT or code not in self.known:
            return {"result": False, "inactive": None, "display": None, "message": "unknown code", "reason": None}
        inactive = code not in self.active
        reason = INACTIVATION_REASONS.get(self.inactivation.get(code, ""), self.inactivation.get(code)) if inactive else None
        return {"result": not inactive, "inactive": inactive, "display": self.pt.get(code, ""), "message": None, "reason": reason}

    def lookup(self, system: str, code: str, version: str, properties: Iterable[str] = ("inactive",)) -> dict:
        v = self.validate(system, code, version)
        if v["inactive"] is None:
            return {"display": None, "properties": {}, "found": False}
        return {"display": v["display"], "properties": {"inactive": [v["inactive"]]}, "found": True}

    def sct_successors(self, code: str, version: str) -> List[dict]:
        self.calls += 1
        return [{"association": HISTORICAL_ASSOCIATIONS[rs], "code": t, "display": self.pt.get(t, "")}
                for rs, t in self.assoc.get(code, [])]


class Router:
    """Dispatch SNOMED CT calls for versions held in RF2 archives to them, everything else to the server."""

    def __init__(self, server: TerminologyServer, releases: Iterable[Rf2Release]) -> None:
        self.server = server
        self.rf2 = {r.version: r for r in releases}
        self.base = server.base + "".join(f" + {r.base}" for r in self.rf2.values())

    @property
    def calls(self) -> int:
        return self.server.calls + sum(r.calls for r in self.rf2.values())

    def _pick(self, system: str, version: Optional[str]):
        return self.rf2.get(version) if system == SCT and version in self.rf2 else self.server

    def code_system_versions(self, system: str) -> List[str]:
        vs = set(self.server.code_system_versions(system))
        for r in self.rf2.values():
            vs |= set(r.code_system_versions(system))
        return sorted(vs)

    def expand(self, valueset: dict, force_versions: Dict[str, str], page: int = 50000, max_total: int = 500000,
               properties: Iterable[str] = ("inactive",), soft_versions: Optional[Dict[str, str]] = None) -> Tuple[Dict[str, dict], dict]:
        ver = (force_versions or {}).get(SCT) or (soft_versions or {}).get(SCT)
        local = self.rf2.get(ver)
        comp = valueset.get("compose", {})
        if not local or not any(i.get("system") == SCT for i in comp.get("include", [])):
            return self.server.expand(valueset, force_versions, page, max_total, properties, soft_versions)

        def part(keep_sct: bool) -> dict:
            vs = {k: v for k, v in valueset.items() if k != "compose"}
            vs["compose"] = {k: [i for i in comp.get(k, []) if (i.get("system") == SCT) == keep_sct] for k in ("include", "exclude")}
            vs["compose"] = {k: v for k, v in vs["compose"].items() if v}
            return vs

        contains, info = local.expand(part(True), force_versions, page, max_total, properties, soft_versions)
        if info.get("error"):
            return contains, info
        rest = part(False)
        if rest["compose"].get("include"):
            fv = {s: v for s, v in (force_versions or {}).items() if s != SCT}
            sv = {s: v for s, v in (soft_versions or {}).items() if s != SCT}
            more, info2 = self.server.expand(rest, fv, page, max_total, properties, sv)
            if info2.get("error"):
                return contains, info2
            contains.update(more)
            info = {"total": (info["total"] or 0) + (info2["total"] or 0), "truncated": info["truncated"] or info2["truncated"], "error": None}
        return contains, info

    def validate(self, system: str, code: str, version: str) -> dict:
        return self._pick(system, version).validate(system, code, version)

    def lookup(self, system: str, code: str, version: str, properties: Iterable[str] = ("inactive",)) -> dict:
        return self._pick(system, version).lookup(system, code, version, properties)

    def sct_successors(self, code: str, version: str) -> List[dict]:
        return self._pick(SCT, version).sct_successors(code, version)


def make_server(rf2_specs: Iterable[str]) -> "TerminologyServer | Router":
    """rf2_specs: paths to RF2 archives/directories, optionally PATH=VERSION_URI. Empty -> plain server."""
    specs = [s for s in rf2_specs if s]
    server = TerminologyServer()
    if not specs:
        return server
    releases = []
    for s in specs:
        path, _, ver = s.partition("=")
        releases.append(Rf2Release(path, ver or None))
    return Router(server, releases)
