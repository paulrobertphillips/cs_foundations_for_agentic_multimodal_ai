# main.py
from agent import plan_bfs, execute_with_cache
from cache import TaskCache
from tasks import TASKS

task_graph = {
    "prepare_dataset": ["load_data"],
    "load_data": ["validate_schema", "clean_missing"],
    "validate_schema": [],
    "clean_missing": ["compute_features"],
    "compute_features": [],
}

def main():
    print("=== Planning (BFS) ===")
    plan = plan_bfs(task_graph, start="prepare_dataset")
    print("Execution plan:", plan)

    print("\n=== Execution (DFS + Cache) ===")
    cache = TaskCache()
    results = execute_with_cache(task_graph, TASKS, start="prepare_dataset", cache=cache)

    print("\n=== Execution Again (should hit cache) ===")
    results2 = execute_with_cache(task_graph, TASKS, start="prepare_dataset", cache=cache)

    print("\n=== Results ===")
    for k, v in results.items():
        print(f"{k}: {v}")

    print("\n=== Summary ===")
    print(f"Planned {len(plan)} tasks. Executed {len(results)} tasks.")

if __name__ == "__main__":
    main()
