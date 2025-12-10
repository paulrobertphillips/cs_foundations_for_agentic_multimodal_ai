**folder structure**
```
project_root/
    pyproject.toml
    my_agent/
        tools/
            __init__.py
            analysis_tools.py
            io_tools.py      
        agent.py
        config.py
        main.py
        models.py
```

**my_agent/config.py**
```python
from dataclasses import dataclass

@dataclass
class AgentConfig:
    dataset_path: str
    run_summary: bool = True
    run_row_count: bool = True
    run_column_count: bool = True
```

**my_agent/models.py**
```python
from pydantic import BaseModel
from typing import Optional

class SummaryResult(BaseModel):
    mean: float
    std: float

class AnalysisResult(BaseModel):
    row_count: Optional[int] = None
    column_count: Optional[int] = None
    summary: Optional[SummaryResult] = None
```

**my_agent/tools/io_tools.py**
```python
import csv

def load_csv(path: str):
    with open(path, "r") as f:
        return list(csv.DictReader(f))
```

**my_agent/tools/analysis_tools.py**
```python
import asyncio
import statistics

async def count_rows(rows):
    await asyncio.sleep(0)  # pretend async work
    return len(rows)

async def count_columns(rows):
    await asyncio.sleep(0)
    return len(rows[0]) if rows else 0

async def compute_summary(rows):
    await asyncio.sleep(0)
    # Assume dataset has a column named "value"
    values = [float(r["value"]) for r in rows]
    return {
        "mean": statistics.mean(values),
        "std": statistics.stdev(values) if len(values) > 1 else 0.0
    }
```

**my_agent/agent.py**
```python
import asyncio
from .config import AgentConfig
from .tools.io_tools import load_csv
from .tools.analysis_tools import (
    count_rows,
    count_columns,
    compute_summary,
)
from .models import AnalysisResult, SummaryResult

async def run_agent(cfg: AgentConfig) -> AnalysisResult:
    rows = load_csv(cfg.dataset_path)

    tasks = []

    if cfg.run_row_count:
        tasks.append(count_rows(rows))
    if cfg.run_column_count:
        tasks.append(count_columns(rows))
    if cfg.run_summary:
        tasks.append(compute_summary(rows))

    results = await asyncio.gather(*tasks)

    # Map results back to named fields
    output = AnalysisResult()

    idx = 0
    if cfg.run_row_count:
        output.row_count = results[idx]; idx += 1
    if cfg.run_column_count:
        output.column_count = results[idx]; idx += 1
    if cfg.run_summary:
        summary_values = results[idx]
        output.summary = SummaryResult(**summary_values)

    return output
```

**my_agent/main.py**
```python
import asyncio
from .config import AgentConfig
from .agent import run_agent

def main():
    cfg = AgentConfig(dataset_path="data.csv")
    result = asyncio.run(run_agent(cfg))
    # Pydantic model → plain dict
    print(result.model_dump())

if __name__ == "__main__":
    main()
```

**pyproject.toml**
```python
[project]
name = "my_agent"
version = "0.1.0"
description = "Module 0 Micro-Agent Project"
requires-python = ">=3.10"
dependencies = [
    "pydantic>=2.0",
]

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

**Console Output**
```
(.venv) C:\Projects\cs_foundations_for_agentic_multimodal_ai\module_0\project_root>python -m my_agent.main
{'row_count': 5, 'column_count': 1, 'summary': {'mean': 3.0, 'std': 1.5811388300841898}}
```


