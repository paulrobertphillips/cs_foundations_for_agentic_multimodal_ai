# agent.py
from __future__ import annotations

from typing import Any, Callable, Dict, List

from cache import TaskCache
from planner import plan_bfs
from executor import execute_with_cache

TaskFn = Callable[[Dict[str, Any] | None], Dict[str, Any]]

"""
Most commonly planning + execution is defined as part of agent (orchestration)
layer. However, at scale these things would be stored as separate modules/classes.
This is because this layer owns "control flow"

Organization at scale would look something like this, however logic is still
handled at this "agent" layer.
 -> planner.py (planning policy)
 -> executor.py (execution engine)
 -> memory.py (cache + artifact store)
 -> agent.py (wires them together)
"""

def plan(graph: Dict[str, List[str]], start: str) -> List[str]:
    """Agent-level planning API (delegates to planner)."""
    return plan_bfs(graph, start=start)

def run(
    graph: Dict[str, List[str]],
    tasks: Dict[str, Callable[..., Dict[str, Any]]],
    start: str,
    cache: TaskCache,
) -> Dict[str, Dict[str, Any]]:
    """Agent-level execution API (delegates to executor)."""
    return execute_with_cache(graph, tasks, start=start, cache=cache)
