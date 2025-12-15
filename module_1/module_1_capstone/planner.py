# planner.py
from __future__ import annotations

from collections import deque
from typing import Dict, List, Set

def plan_bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    BFS traversal from a starting node.
    Planner view: what becomes reachable next from a goal.

    Converts dynamic dictionary (containing tasks & dependencies) into
    flattened list that will be interated on for execution of tasks.
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
