from dataclasses import dataclass
from typing import Dict, List

@dataclass
class AgentRunResult:
    execution_order: List[str]
    results: Dict[str, object]