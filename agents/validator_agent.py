"""Validator acts as schema and simple sanity checker."""

from typing import Any, Dict, List

from tools.data_store import append_rows

REQUIRED_FIELDS = [
    "Location",
    "Specialty",
    "Risk Level",
    "Language Name",
    "Language Family",
    "Cultural Practices",
    "Revitalization Efforts",
    "Geographic Coordinates",
    "Historical Context",
]


def _has_required_fields(rec: Dict[str, Any]) -> bool:
    for field in REQUIRED_FIELDS:
        if field not in rec:
            return False
        if not str(rec[field]).strip():
            return False
    return True


def _coords_valid(rec: Dict[str, Any]) -> bool:
    coords = str(rec.get("Geographic Coordinates", "")).strip()
    if "," not in coords:
        return False
    lat_str, lon_str = [x.strip() for x in coords.split(",", 1)]
    try:
        lat = float(lat_str)
        lon = float(lon_str)
    except ValueError:
        return False
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        return False
    return True


def is_valid_record(rec: Dict[str, Any]) -> bool:
    if not _has_required_fields(rec):
        return False
    if not _coords_valid(rec):
        return False
    return True


def validate_and_commit(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filters records through validation rules and appends valid ones to the CSV.
    Returns the list of committed records.
    """
    valid = [r for r in records if is_valid_record(r)]
    if valid:
        append_rows(valid)
    return valid
