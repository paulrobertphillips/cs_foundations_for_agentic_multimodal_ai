# 🧠 Module 0 Capstone: The Async EDA Micro-Agent


Let’s build your Module 0 Micro-Agent Project — a small but meaningful agent that uses every concept you learned:
- Python packaging & modules
- virtual environment
- dataclasses
- Pydantic models
- async functions & concurrency
- clean folder structure and imports
This will feel like your first “real” agentic system, just simplified.

### 🎯 Goal

Build a tiny agent that:
1. Loads a dataset (CSV)
2. Validates a user-provided configuration (Pydantic)
3. Runs multiple analysis tasks concurrently (async)
4. Uses a dataclass to store agent config
5. Outputs results as a Pydantic model
This mirrors the core flow of many agent pipelines used in AI-for-science.
---

### 📁 Folder Structure (Recommended)

```
project_root/
    pyproject.toml
    my_agent/
        __init__.py
        config.py            ← dataclass-based agent configuration
        models.py            ← Pydantic schemas for results
        tools/
            __init__.py
            io_tools.py      ← load CSV
            analysis_tools.py← async analysis functions
        agent.py             ← orchestrates async tasks
        main.py              ← runs the micro-agent

```
This mirrors the layout of real agent frameworks.

Copy each file’s code into your project:
- `config.py` → dataclass
- `models.py` → Pydantic schemas
- `tools/io_tools.py` → CSV loader
- `tools/analysis_tools.py` → async tasks
- `agent.py` → async orchestrator
- `main.py` → entrypoint runner
This is your agent’s “brain.”
---

### 🔧 1. Define a Config Dataclass

**my_agent/config.py**
```
from dataclasses import dataclass

@dataclass
class AgentConfig:
    dataset_path: str
    run_summary: bool = True
    run_row_count: bool = True
    run_column_count: bool = True

```
This matches how agent configurations are stored in LangChain, Autogen, Swarm, etc.

---

### 🔧 2. Define Pydantic Result Models

**my_agent/models.py**
```
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
Pydantic gives us well-typed, validated outputs.

---

### 🔧 3. Build Tools (I/O + async analysis)


I/O Tool

**my_agent/tools/io_tools.py**
```
import csv

def load_csv(path: str):
    with open(path, "r") as f:
        return list(csv.DictReader(f))

```

Async Analysis Tools

**my_agent/tools/analysis_tools.py**
```
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
Note: the fake sleeps simulate async; real agents would be calling APIs or tools.

---

### 🤖 4. Create the Agent (Async Orchestrator)

**my_agent/agent.py**
```
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
This block demonstrates:
- async orchestration
- dynamic task scheduling
- mapping results to typed models
- clean layering of I/O, compute, models, agent logic
---

### 🎬 5. Entry Point

**my_agent/main.py**
```
import asyncio
from .config import AgentConfig
from .agent import run_agent

if __name__ == "__main__":
    cfg = AgentConfig(dataset_path="data.csv")
    result = asyncio.run(run_agent(cfg))
    print(result.model_dump())

```

---

### 🔧 6. Create your pyproject.toml

Something like:
```
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
Keep it simple — Module 0 is about foundations.

---

### 🔧 7.  Install your project in editable mode

From the folder that contains pyproject.toml:
```
pip install -e .

```
This is where most packaging errors show up, and if they do, we’ll fix them together.
---

### 🔧 8.  Create a simple data.csv

Example:
```
value
1
2
3
4
5

```
Place it in the project root or specify a full path in your config.

---

### 🔧 9.  Run the micro-agent


In your venv:
```
python -m my_agent.main

```
or just:
```
python my_agent/main.py

```
Expected output:
```
{'row_count': 5, 'column_count': 1, 'summary': {'mean': 3.0, 'std': 1.5811}}

```

---

### 🧩 When you’re done…

Reply here with:

✔️ Your folder layout


✔️ Your code (you can paste each file as you did before)


✔️ The console output


✔️ Any errors you hit (if something breaks)

I will:
- review your structure
- validate your implementation
- help debug anything
- tune the design like a software engineer reviewing a junior engineer’s PR
- optionally help you extend the agent with additional tools or behaviors