# executor.py
from __future__ import annotations

from typing import Any, Callable, Dict, List, Tuple

from cache import TaskCache

def execute_with_cache(
    graph: Dict[str, List[str]],
    tasks: Dict[str, Callable[..., Dict[str, Any]]],
    start: str,
    cache: TaskCache,
) -> Tuple[Dict[str, Dict[str, Any]], List[str], List[str]]:
    """
    Execute tasks using DFS-style traversal from the root, passing each task's
    output artifact to its downstream children. Uses memoization to reuse results.

    Returns:
      results: task_name -> output artifact
      cache_hits: list of cache keys hit (task:dataset_path)
      executed_order: list of task names visited (DFS order)
    """
    results: Dict[str, Dict[str, Any]] = {}
    cache_hits: List[str] = []
    executed_order: List[str] = []

    def make_cache_key(task_name: str, artifact_in: Dict[str, Any] | None) -> str:
        dataset_path = artifact_in.get("dataset_path") if artifact_in else None
        return f"{task_name}:{dataset_path or 'none'}"

    def run(task_name: str, artifact_in: Dict[str, Any] | None) -> Dict[str, Any]:
        cache_key = make_cache_key(task_name, artifact_in)

        # Record visit order (only once per task_name)
        if task_name not in executed_order:
            executed_order.append(task_name)

        # Cache hit: reuse output, still traverse children
        if cache.has(cache_key):
            cache_hits.append(cache_key)
            print(f"[CACHE HIT] {cache_key}")
            output = cache.get(cache_key)  # type: ignore[assignment]
            results[task_name] = output  # type: ignore[assignment]

            for child in graph.get(task_name, []):
                run(child, output)  # type: ignore[arg-type]

            return output  # type: ignore[return-value]

        """
        Check if called task has been defined in agent under tasks.py
        """
        # Execute task
        if task_name not in tasks:
            raise KeyError(f"No task function registered for '{task_name}'")

        """
         - Select funtion from TASKS mapping & execute function
         - Artifact is appended upon per task executed, starts as None
        """
        fn = tasks[task_name]
        output = fn(artifact_in)

        # Store result
        cache.set(cache_key, output)
        results[task_name] = output

        # DFS to children -> return empty list if not found
        for child in graph.get(task_name, []):
            run(child, output)

        return output

    """
    With initial call artifact is None because
    no tasks have been executed yet!

    Initial call just sets up DFS logic
    """
    run(start, None)
    return results, cache_hits, executed_order
