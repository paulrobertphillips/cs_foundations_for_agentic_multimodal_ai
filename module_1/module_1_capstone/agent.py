# agent.py
from __future__ import annotations

from collections import deque
from typing import Any, Callable, Dict, List, Set

from cache import TaskCache

TaskFn = Callable[[Dict[str, Any] | None], Dict[str, Any]]

def plan_bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    BFS traversal from a starting node.
    This is a *planning view* of the workflow: what becomes reachable next.
    """
    visited: Set[str] = set()
    q = deque([start])
    order: List[str] = []

    while q:
        node = q.popleft()
        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        for nxt in graph.get(node, []):
            if nxt not in visited:
                q.append(nxt)

    return order

def execute_with_cache(
    graph: Dict[str, List[str]],
    tasks: Dict[str, Callable[..., Dict[str, Any]]],
    start: str,
    cache: TaskCache,
) -> Dict[str, Dict[str, Any]]:
    """
    Execute tasks using DFS-style traversal from the root, passing the
    output artifact of each task to its downstream children.

    Returns: dict mapping task_name -> task_output_artifact
    """
    def make_cache_key(task_name: str, artifact_in: Dict[str, Any] | None) -> str:
        dataset_path = artifact_in.get("dataset_path") if artifact_in else None
        return f"{task_name}:{dataset_path or 'none'}"
    
    results: Dict[str, Dict[str, Any]] = {}

    def run(task_name: str, artifact_in: Dict[str, Any] | None) -> Dict[str, Any]:
        cache_key = make_cache_key(task_name, artifact_in)

        # Cache hit: reuse output, still traverse children
        if cache.has(cache_key):
            print(f"[CACHE HIT] {cache_key}")
            output = cache.get(cache_key)  # type: ignore[assignment]

            # Make sure cached outputs appear in results too
            results[task_name] = output  # type: ignore[assignment]

            for child in graph.get(task_name, []):
                run(child, output)  # type: ignore[arg-type]

            return output  # type: ignore[return-value]

        # Execute task
        if task_name not in tasks:
            raise KeyError(f"No task function registered for '{task_name}'")

        fn = tasks[task_name]
        output = fn(artifact_in)

        # Store result
        cache.set(cache_key, output)
        results[task_name] = output

        # DFS to children (graph uses task_name keys)
        for child in graph.get(task_name, []):
            run(child, output)

        return output

    # Start at the root goal node with no prior artifact
    run(start, None)
    return results
