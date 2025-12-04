"""Research agent does tool augmented LLM calls and returns records."""

import json
from typing import Any, Dict, List, Tuple

from tools.llm_client import call_llm
from tools.data_store import load_tasks, save_tasks

SYSTEM_PROMPT = """
You are a linguistic and anthropological research agent focused on endangered and vulnerable languages in the Americas.

Your goals:
1. Identify real languages or language varieties with some evidence in the public record.
2. Produce structured records that follow the required schema exactly.
3. Use cautious language about uncertainty. Do not invent specific revitalization programs or institutions if you do not know they exist.
4. Output only JSON, no commentary, no markdown.

Every record must have these exact keys:
Location, Specialty, Risk Level, Language Name, Language Family, Dialects,
Cultural Practices, Revitalization Efforts, Geographic Coordinates, Historical Context.

Geographic Coordinates must be a simple string of the form "lat, lon".
Use degrees in decimal representation where possible.
"""

USER_TEMPLATE = """
Research 1 to 3 endangered or vulnerable languages in this region.

Region: {region}
Focus: {notes}

Return ONLY a JSON array in this exact format:

[
  {{
    "Location": "Region name or description",
    "Specialty": "Indigenous Language Preservation",
    "Risk Level": "High Risk",
    "Language Name": "Language name",
    "Language Family": "Family name",
    "Dialects": "Short description of major dialects or varieties",
    "Cultural Practices": "Relevant cultural practices and traditions linked to this language",
    "Revitalization Efforts": "Known or likely revitalization efforts. Use cautious language and avoid naming specific programs unless you are reasonably confident they exist.",
    "Geographic Coordinates": "lat, lon",
    "Historical Context": "Concise historical context on the language and community"
  }}
]
"""


def _parse_records(raw: str) -> List[Dict[str, Any]]:
    """
    Try to parse LLM output as JSON array.
    If it fails, return an empty list.
    """
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            return data
        return []
    except json.JSONDecodeError:
        return []


def take_next_research_task() -> Tuple[Dict[str, Any] | None, List[Dict[str, Any]]]:
    """
    Pops the next research task from the queue and returns (task, records).
    If no valid research task is available, returns (None, []).
    """
    tasks = load_tasks()
    if not tasks:
        return None, []

    # Simple FIFO queue for now
    task = tasks.pop(0)

    # Persist the updated queue immediately
    save_tasks(tasks)

    if task.get("type") != "research_language":
        return None, []

    user_prompt = USER_TEMPLATE.format(
        region=task.get("target_region", ""),
        notes=task.get("notes", ""),
    )

    raw = call_llm(SYSTEM_PROMPT, user_prompt)
    records = _parse_records(raw)

    return task, records
