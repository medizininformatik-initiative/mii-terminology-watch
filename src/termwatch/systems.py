"""Code-system registry: which systems are watched and how each one behaves.

Everything else in termwatch is generic.  A system not listed here still works
with the generic adapter (validate-code for status, no successors); listing it
only adds a short key, a label and the system-specific tricks.
"""
from __future__ import annotations

import re
from typing import Dict, List, Optional

SCT = "http://snomed.info/sct"
LOINC = "http://loinc.org"
ICD10GM = "http://fhir.de/CodeSystem/bfarm/icd-10-gm"
OPS = "http://fhir.de/CodeSystem/bfarm/ops"
ATC = "http://fhir.de/CodeSystem/bfarm/atc"
HGNC = "http://www.genenames.org/geneId"
ALPHAID = "http://fhir.de/CodeSystem/bfarm/alpha-id"
ORPHA = "http://www.orpha.net"
UCUM = "http://unitsofmeasure.org"

# status: how the status of a code that left the expansion is determined
#   "validate"  -> CodeSystem/$validate-code (result + inactive flag); generic default
#   "lookup"    -> CodeSystem/$lookup with status_property (LOINC STATUS)
# successors: "sct" -> SNOMED historical-association ConceptMaps; None otherwise
# anchors: True -> is-a / descendent-of filter values are validated as anchors
# yearly: one release per year (BfArM classifications); only affects wording
REGISTRY: Dict[str, dict] = {
    SCT:     {"key": "sct",     "label": "SNOMED CT", "status": "validate", "successors": "sct", "anchors": True},
    LOINC:   {"key": "loinc",   "label": "LOINC",     "status": "lookup", "status_property": "STATUS"},
    ICD10GM: {"key": "icd10gm", "label": "ICD-10-GM", "status": "validate", "yearly": True},
    OPS:     {"key": "ops",     "label": "OPS",       "status": "validate", "yearly": True},
    ATC:     {"key": "atc",     "label": "ATC",       "status": "validate", "yearly": True},
    HGNC:    {"key": "hgnc",    "label": "HGNC",      "status": "validate"},
    ALPHAID: {"key": "alphaid", "label": "Alpha-ID",  "status": "validate", "yearly": True},
    ORPHA:   {"key": "orpha",   "label": "Orphanet",  "status": "validate", "yearly": True},
    UCUM:    {"key": "ucum",    "label": "UCUM",      "status": "validate"},
}
DEFAULT_WATCHED: List[str] = [SCT, LOINC, ICD10GM, OPS, ATC, HGNC]


def spec(system: str) -> dict:
    if system in REGISTRY:
        return REGISTRY[system]
    slug = re.sub(r"[^a-z0-9]+", "-", system.lower().split("//")[-1]).strip("-")
    return {"key": slug, "label": system, "status": "validate"}


def key_of(system: str) -> str:
    return spec(system)["key"]


def label_of(system: str) -> str:
    return spec(system)["label"]


def system_for(key_or_url: str) -> str:
    """Accept a registry key ("icd10gm"), a URL, or a URL of a watched system."""
    if key_or_url.startswith("http"):
        return key_or_url
    for url, s in REGISTRY.items():
        if s["key"] == key_or_url:
            return url
    raise ValueError(f"unknown code system key {key_or_url!r}; use a URL or one of {[s['key'] for s in REGISTRY.values()]}")


def parse_watch(arg: Optional[str]) -> List[str]:
    if not arg:
        return list(DEFAULT_WATCHED)
    if arg.strip() == "all":
        return list(REGISTRY)
    return [system_for(x.strip()) for x in arg.split(",") if x.strip()]


def parse_versions(pairs: List[str]) -> Dict[str, str]:
    """--system key=version or --system URL=version (repeatable)."""
    out: Dict[str, str] = {}
    for p in pairs or []:
        if "=" not in p:
            raise ValueError(f"--system expects KEY=VERSION or URL=VERSION, got {p!r}")
        k, v = p.split("=", 1)
        out[system_for(k.strip())] = v.strip()
    return out


def short_version(system: str, version: Optional[str]) -> str:
    """Human-readable release label: SNOMED version URIs become their date."""
    if not version:
        return "?"
    if system == SCT:
        m = re.search(r"/version/(\d{8})$", version)
        return m.group(1) if m else version
    return version


def version_sort_key(v: str):
    parts = re.findall(r"\d+", v or "")
    return [int(p) for p in parts] or [0]
