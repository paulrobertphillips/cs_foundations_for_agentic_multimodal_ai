# models.py
from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class RunReport:
    plan: List[str]
    executed_order: List[str]
    cache_hits: List[str]          # store cache keys like "load_data:data.csv"
    results: Dict[str, Dict[str, Any]]
