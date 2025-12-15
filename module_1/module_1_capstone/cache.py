# cache.py
from typing import Any, Dict, Optional

class TaskCache:
    """
    Simple in-memory cache for task results.
    This mimics "agent memory" for expensive/repeatable computations.
    """
    def __init__(self) -> None:
        self._cache: Dict[str, Any] = {}

    def has(self, key: str) -> bool:
        return key in self._cache

    def get(self, key: str) -> Optional[Any]:
        return self._cache.get(key)

    def set(self, key: str, value: Any) -> None:
        self._cache[key] = value
