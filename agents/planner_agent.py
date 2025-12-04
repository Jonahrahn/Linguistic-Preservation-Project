"""Planner identifies coverage gaps and creates tasks. This is your constraint brain."""

import uuid
from collections import Counter
from typing import List, Dict, Any

from tools.data_store import load_rows, load_tasks, save_tasks

TARGET_REGIONS = [
    "Amazon Basin",
    "Andes",
    "Mesoamerica",
    "Arctic",
    "Caribbean",
    "Great Plains",
    "Pacific Northwest",
    "Patagonia",
]


def plan_new_tasks(max_new_tasks: int = 5) -> List[Dict[str, Any]]:
    """
    Planner agent.
    Looks at current coverage per region and emits new research tasks
    for regions with the lowest coverage.
    """
    rows = load_rows()
    tasks = load_tasks()

    existing_regions = [
        r.get("Location", "").strip()
        for r in rows
        if r.get("Location", "").strip()
    ]
    counts = Counter(existing_regions)

    # Sort regions by current coverage ascending
    region_order = sorted(TARGET_REGIONS, key=lambda r: counts.get(r, 0))

    new_tasks = []

    for region in region_order:
        already_planned = any(
            t.get("type") == "research_language"
            and t.get("target_region") == region
            for t in tasks
        )
        if already_planned:
            continue

        new_task = {
            "task_id": f"task-{uuid.uuid4().hex[:8]}",
            "type": "research_language",
            "target_region": region,
            "notes": "Focus on endangered or critically endangered languages. Avoid fabricating programs. Use cautious phrasing where sources are uncertain.",
        }
        new_tasks.append(new_task)

        if len(new_tasks) >= max_new_tasks:
            break

    if new_tasks:
        tasks.extend(new_tasks)
        save_tasks(tasks)

    return new_tasks
