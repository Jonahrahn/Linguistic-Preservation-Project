"""Main loop that coordinates agents and prints some progress."""

from agents.planner_agent import plan_new_tasks
from agents.research_agent import take_next_research_task
from agents.validator_agent import validate_and_commit
from tools.data_store import load_rows


def run_agentic_cycle(max_planning_tasks: int = 5, max_iterations: int = 10) -> None:
    """
    End to end agentic loop:
    1. Planner identifies gaps and creates new research tasks.
    2. Research agent works through the queue.
    3. Validator enforces schema and writes valid entries to CSV.
    """
    print("Starting agentic cycle")

    new_tasks = plan_new_tasks(max_new_tasks=max_planning_tasks)
    print(f"Planner created {len(new_tasks)} new tasks")

    iterations = 0

    while iterations < max_iterations:
        iterations += 1

        task, records = take_next_research_task()
        if task is None:
            print("No research tasks left in queue")
            break

        print(f"[{iterations}] Working on task {task.get('task_id')} for region {task.get('target_region')}")

        if not records:
            print("No records returned or parse failure, skipping")
            continue

        committed = validate_and_commit(records)
        print(f"Committed {len(committed)} records")

    rows = load_rows()
    print(f"Total records in dataset: {len(rows)}")


if __name__ == "__main__":
    run_agentic_cycle(max_planning_tasks=5, max_iterations=10)
