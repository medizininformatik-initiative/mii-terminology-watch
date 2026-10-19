"""Build the specification inventory from a FHIR package directory."""
from __future__ import annotations

import copy
import glob
import json
import os
import re
from typing import Dict, List, Optional

from .systems import DEFAULT_WATCHED

GROUP_MII = "mii"


def group_of(vs: dict, strategy: str = GROUP_MII, package_name: str = "") -> str:
    """Group a ValueSet into a lane set ("module").

    strategy: "mii" (modul-<name> in the canonical or mii-vs-<name> in the id),
    "package" (one group per package), "host" (canonical host), or a regular
    expression with one capturing group applied to the canonical URL.
    """
    url = vs.get("url", "")
    if strategy == GROUP_MII:
        m = re.search(r"/modul-([a-z0-9-]+)/", url) or re.search(r"mii-vs-([a-z]+)", vs.get("id", ""))
        return m.group(1) if m else (url.split("/")[2] if url.startswith("http") else "unknown")
    if strategy == "package":
        return package_name or "package"
    if strategy == "host":
        return url.split("/")[2] if url.startswith("http") else "unknown"
    m = re.search(strategy, url)
    return m.group(1) if m and m.groups() else "other"


def drop_pinned_of_multi(vs: dict, multi_systems: List[str]) -> dict:
    """For systems the ValueSet pins in several versions (unions of yearly releases),
    keep only the unpinned includes: pinned yearly includes never change with a new
    release, and expanding 17 years of OPS just to diff the unpinned part is wasteful."""
    if not multi_systems:
        return vs
    vs = copy.deepcopy(vs)
    comp = vs.setdefault("compose", {})
    comp["include"] = [i for i in comp.get("include", []) if not (i.get("system") in multi_systems and i.get("version"))]
    return vs


def version_modes(entry: dict, versions: Dict[str, str]) -> "tuple[Dict[str, str], Dict[str, str]]":
    """Split the versions to apply into forced and soft ones.

    A system is forced unless the ValueSet pins several different versions of
    it (e.g. a union of yearly ICD-10-GM releases); then only the unpinned
    includes follow the requested version.
    """
    force, soft = {}, {}
    for s in entry["systems"]:
        if s not in versions:
            continue
        pins = {i["version"] for i in entry["includes"] if i["system"] == s and i.get("version")}
        (soft if len(pins) > 1 else force)[s] = versions[s]
    return force, soft


def load_package(package_dir: str) -> Dict[str, dict]:
    """Return canonical url -> ValueSet for every ValueSet in the package."""
    out: Dict[str, dict] = {}
    for f in glob.glob(os.path.join(package_dir, "ValueSet-*.json")):
        try:
            vs = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if vs.get("resourceType") == "ValueSet" and vs.get("url"):
            out[vs["url"]] = vs
    return out


def inline_valueset_refs(vs: dict, by_url: Dict[str, dict], depth: int = 0) -> dict:
    """Replace compose.include.valueSet references with the referenced includes (package-local only)."""
    vs = copy.deepcopy(vs)
    if depth > 5:
        return vs
    new_includes: List[dict] = []
    for inc in vs.get("compose", {}).get("include", []):
        refs = inc.get("valueSet")
        if refs and not inc.get("system"):
            for ref in refs:
                target = by_url.get(ref.split("|")[0])
                if target:
                    new_includes.extend(inline_valueset_refs(target, by_url, depth + 1)["compose"]["include"])
                else:
                    new_includes.append(inc)  # unresolved, let the server try
        else:
            new_includes.append(inc)
    vs.setdefault("compose", {})["include"] = new_includes
    return vs


def restrict_to_watched(vs: dict, watched: Optional[List[str]] = None) -> dict:
    """Keep only includes/excludes of watched systems; others are out of scope and may not exist on the server."""
    watched = set(watched or DEFAULT_WATCHED)
    vs = copy.deepcopy(vs)
    comp = vs.setdefault("compose", {})
    comp["include"] = [i for i in comp.get("include", []) if i.get("system") in watched]
    if comp.get("exclude"):
        comp["exclude"] = [i for i in comp["exclude"] if i.get("system") in watched]
    vs.pop("expansion", None)
    # supplements (valueset-supplement extension) are usually not loaded on the server; drop them for expansion
    if vs.get("extension"):
        vs["extension"] = [x for x in vs["extension"] if x.get("url") != "http://hl7.org/fhir/StructureDefinition/valueset-supplement"] or None
        if vs["extension"] is None:
            vs.pop("extension")
    return vs


def build_inventory(package_dir: str, watched: Optional[List[str]] = None, group: str = GROUP_MII) -> dict:
    watched = list(watched or DEFAULT_WATCHED)
    pj = json.load(open(os.path.join(package_dir, "package.json"), encoding="utf-8"))
    by_url = load_package(package_dir)
    entries: List[dict] = []
    for url, vs in sorted(by_url.items()):
        includes = []
        for inc in vs.get("compose", {}).get("include", []):
            sys_ = inc.get("system")
            if sys_ not in watched:
                continue
            kind = "filter" if inc.get("filter") else "enumerated" if inc.get("concept") else "whole-system"
            includes.append({
                "system": sys_, "kind": kind, "version": inc.get("version"),
                "concepts": [c["code"] for c in inc.get("concept", [])],
                "filters": inc.get("filter", []),
            })
        if not includes:
            continue
        entries.append({
            "id": vs.get("id"), "url": url, "version": vs.get("version"), "title": vs.get("title") or vs.get("name"),
            "module": group_of(vs, group, pj.get("name", "")), "status": vs.get("status"),
            "systems": sorted({i["system"] for i in includes}),
            "pinned": all(i["version"] for i in includes),
            "multi_version": sorted({i["system"] for i in includes
                                     if len({j["version"] for j in includes if j["system"] == i["system"] and j.get("version")}) > 1}),
            "includes": includes,
            "has_valueset_refs": any(i.get("valueSet") for i in vs.get("compose", {}).get("include", [])),
        })
    return {
        "package": {"name": pj.get("name"), "version": pj.get("version"), "fhirVersion": pj.get("fhirVersions") or pj.get("fhir-version-list")},
        "watched": watched, "group": group,
        "valuesets": entries,
    }
