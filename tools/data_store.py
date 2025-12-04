import csv
import json
from pathlib import Path
from typing import List, Dict, Any

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True)

CSV_FILE = DATA_PATH / "cultural_data.csv"
TASK_FILE = DATA_PATH / "task_queue.json"

CSV_FIELDS = [
    "Location",
    "Specialty",
    "Risk Level",
    "Language Name",
    "Language Family",
    "Dialects",
    "Cultural Practices",
    "Revitalization Efforts",
    "Geographic Coordinates",
    "Historical Context",
]


def init_csv_if_needed() -> None:
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()


def load_rows() -> List[Dict[str, Any]]:
    init_csv_if_needed()
    with CSV_FILE.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def append_rows(rows: List[Dict[str, Any]]) -> None:
    if not rows:
        return
    init_csv_if_needed()
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        for row in rows:
            writer.writerow(row)


def load_tasks() -> List[Dict[str, Any]]:
    if not TASK_FILE.exists():
        return []
    with TASK_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    with TASK_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
