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

    cache = TaskCache()

    """
    Notes
     -> Caching can be short-term memory (in-memory) or long-term memory (external)
     -> Since caching can be long-term memory (external), needs to be passed as parameter
     -> Mapping of DAG to functions themselves has to be predefined (e.g., TASKS)
     -> Remember, what you get out of doing work is called an "artifact" -> what's tangible
        => Result of each task is added to artifact
    """

    print("=== Run 1 ===")
    report1 = run(task_graph, TASKS, start="prepare_dataset", cache=cache)

    print("\nPlan:")
    for step in report1.plan:
        print(" -", step)
    
    print("\nExecuted order (DFS):")
    for step in report1.executed_order:
        print(" -", step)
    
    print("\nCache hits:", report1.cache_hits)

    print("\nResults:")
    for k, v in report1.results.items():
        print(f"{k}: {v}")

    print("\n=== Run 2 (should hit cache) ===")
    report2 = run(task_graph, TASKS, start="prepare_dataset", cache=cache)
    print("Cache hits:", report2.cache_hits)

    print("\n=== Summary ===")
    print(f"Planned {len(report2.plan)} tasks. Executed {len(report2.executed_order)} tasks.")
    print(f"Cache hits: {len(report2.cache_hits)}")

if __name__ == "__main__":
    main()
