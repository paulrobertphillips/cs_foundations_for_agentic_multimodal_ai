# main.py
from agent import plan, run
from cache import TaskCache
from tasks import TASKS

"""
Where BFS/DFS "live" conceptually
Think in layers:
    -> Graph / State representation (what exists) - task_graph, nodes/edges
    -> Planning logic (decide what to do) - BFS-like (or other planners)
    -> Execution logic (do it) - DFS-like dependency resolution (traversal)
    -> Caching / memory (don't repeat work) - memoization, artifact stores
    -> Tools (actual work) - loading data, cleaning, etc.
"""

task_graph = {
    "prepare_dataset": ["load_data"],
    "load_data": ["validate_schema", "clean_missing"],
    "validate_schema": [],
    "clean_missing": ["compute_features"],
    "compute_features": [],
}

def main():

    print("=== Planning (BFS) ===")
    plan_list = plan(task_graph, start="prepare_dataset")
    print("Execution plan:")
    for step in plan_list:
        print(" -", step)


    print("\n=== Execution (DFS + Cache) ===")
    """
    Notes
     -> Caching can be short-term memory (recursive) or long-term memory (external)
     -> Since caching can be long-term memory (external), needs to be passed as parameter
     -> Mapping of DAG to functions themselves has to be predefined (e.g., TASKS)
     -> Remember, what you get out of doing work is called an "artifact" -> what's tangible
        => Result of each task is added to artifact
    """
    cache = TaskCache()
    results = run(task_graph, TASKS, start="prepare_dataset", cache=cache)

    print("\n=== Execution Again (should hit cache) ===")
    results2 = run(task_graph, TASKS, start="prepare_dataset", cache=cache)

    print("\n=== Results ===")
    for k, v in results.items():
        print(f"{k}: {v}")

    print("\n=== Summary ===")
    print(f"Planned {len(plan_list)} tasks. Executed {len(results)} tasks.")

if __name__ == "__main__":
    main()
