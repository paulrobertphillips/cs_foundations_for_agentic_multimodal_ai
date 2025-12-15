# 🏁 **MODULE 1 CAPSTONE — Data Preparation Planning Agent**

## 🎯 Capstone Goal

Build a **simple agent** that:

1. Accepts a **data-preparation task DAG**
2. **Plans** a valid execution order (BFS-style reasoning)
3. **Executes** tasks in order (DFS-style execution)
4. Uses **caching (dynamic programming)** to avoid recomputing results
5. Returns a **structured result** describing:

   * execution order
   * task outputs
   * cached reuse (where applicable)

This mirrors how real-world data pipelines and agentic systems operate.

---

## 🧠 What This Capstone Demonstrates

This project explicitly ties together:

| Module Concept      | Where It Appears               |
| ------------------- | ------------------------------ |
| Graphs / DAGs       | Task dependency representation |
| BFS                 | Planning valid execution order |
| DFS                 | Executing tasks deeply         |
| Recursion           | Subtask execution              |
| Dynamic Programming | Caching task outputs           |
| Modular design      | Clean, refactorable code       |

This is **agentic thinking**, not just scripting.

---

## 📁 Suggested Folder Structure

You can follow this (flexible, not strict):

```
module_1_capstone/
    agent.py
    tasks.py
    cache.py
    models.py
    main.py
```

---

## 📋 Step 1 — Define the Task DAG

Use a **data preparation pipeline** you already know well:

```python
task_graph = {
    "prepare_dataset": ["load_data"],
    "load_data": ["validate_schema", "clean_missing"],
    "validate_schema": [],
    "clean_missing": ["compute_features"],
    "compute_features": []
}
```

This is your **planning space**.

---

## 📋 Step 2 — Define Task Functions (Execution Layer)

In `tasks.py`, define simple task functions.

Example:

```python
def load_data():
    return {"rows": 100, "columns": 5}

def validate_schema(data):
    return True

def clean_missing(data):
    return {"rows": 95, "columns": 5}

def compute_features(data):
    return {"features": ["f1", "f2", "f3"]}
```

These are deliberately simple — focus is on *control flow*, not data wrangling.

---

## 📋 Step 3 — Add a Cache (Dynamic Programming)

In `cache.py`:

```python
class TaskCache:
    def __init__(self):
        self._cache = {}

    def get(self, task_name):
        return self._cache.get(task_name)

    def set(self, task_name, result):
        self._cache[task_name] = result
```

This is **agent memory**.

---

## 📋 Step 4 — Planning Phase (BFS)

In `agent.py`, write a BFS function that produces a **valid execution order**.

Key ideas:

* queue (`deque`)
* visited set
* start at `"prepare_dataset"`

The output should be something like:

```python
["prepare_dataset", "load_data", "validate_schema", "clean_missing", "compute_features"]
```

This is the **agent’s plan**.

---

## 📋 Step 5 — Execution Phase (DFS + Caching)

Now execute tasks **in order**, using:

* DFS-style recursion
* cached results where available

Pseudocode logic:

```
execute(task):
    if task result cached:
        return cached result

    for dependency:
        execute(dependency)

    run task
    cache result
    return result
```

This is *subproblem decomposition + DP* in action.

---

## 📋 Step 6 — Structured Output

In `models.py`, define a simple result model (dataclass or Pydantic):

```python
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class AgentRunResult:
    execution_order: List[str]
    results: Dict[str, object]
```

Return this from your agent.

---

## 🧪 What to Submit (Like Previous Modules)

When you’re ready, you’ll share:

1. Folder structure
2. Key code snippets (agent + cache + tasks)
3. Console output showing:

   * execution order
   * cached reuse (if you simulate repeated calls)

We’ll then:

* review it together
* refine it slightly
* and formally close **Module 1**

---

## 🧠 Why This Capstone Is Important

After this project, you’ll be able to say:

> “I understand how agents plan workflows, execute tasks, and avoid repeated work — and I can implement it myself.”

That’s a *huge* step forward.

---

## 🔜 Next Action

If you’d like, I can:

* **A)** give you a **minimal starter scaffold** (blank files + TODOs), or
* **B)** walk you through the capstone **step-by-step interactively**, or
* **C)** let you implement it independently and review your solution

Which approach do you want to take?
