from dataclasses import dataclass
from typing import Dict, List

"""
Not actually used in this capstone project,
but idea would be to have returned dictionaries
from planning & executing tasks stored in class
object.
"""

@dataclass
class AgentRunResult:
    execution_order: List[str]
    results: Dict[str, object]