# 🏁 Module 1 Capstone — Interactive Build

## ✅ Step 0 — Folder + Files

Create this folder structure (same level is fine):

```
module_1_capstone/
    main.py
    agent.py
    tasks.py
    cache.py
    models.py
```

No packaging needed unless you want it — keeping it simple for now.

---

## ✅ Step 1 — Define the Task DAG + Entry Point (`main.py`)

Copy/paste:

```python
# main.py
from agent import plan_bfs, execute_with_cache
from cache import TaskCache
from tasks import TASKS

task_graph = {
    "prepare_dataset": ["load_data"],
    "load_data": ["validate_schema", "clean_missing"],
    "validate_schema": [],
    "clean_missing": ["compute_features"],
    "compute_features": [],
}

def main():
    print("=== Planning (BFS) ===")
    plan = plan_bfs(task_graph, start="prepare_dataset")
    print("Execution plan:", plan)

    print("\n=== Execution (DFS + Cache) ===")
    cache = TaskCache()
    results = execute_with_cache(task_graph, TASKS, start="prepare_dataset", cache=cache)

    print("\n=== Results ===")
    for k, v in results.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
```

What this does:

* calls `plan_bfs()` to generate a plan
* calls `execute_with_cache()` to run tasks using DFS-style dependencies + memoization
* prints results

---

## ✅ Your step now

Create the files and paste in `main.py` exactly as above.

Don’t run yet — we still need `agent.py`, `tasks.py`, `cache.py`.

When you’ve got that, say **“Step 1 done”** and we’ll move to Step 2 (implementing the cache).

Nice — onward.

---

## ✅ Step 2 — Add the Cache (`cache.py`)

Copy/paste this into `cache.py`:

```python
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
```

Notes:

* `key` will be the task name (e.g., `"load_data"`)
* later, we can upgrade this to key on `(task_name, input_hash)` if we want more realism

---

### ✅ Your step now

Create `cache.py` with the above.

When done, say **“Step 2 done”** and we’ll implement the task functions in Step 3.

Great — now we’ll build the “tool layer” for the agent.

---

## ✅ Step 3 — Define Tasks (`tasks.py`)

These tasks are intentionally simple, but they mimic real data-prep stages by passing a shared “data artifact” forward.

Copy/paste into `tasks.py`:

```python
# tasks.py
from typing import Any, Dict

def prepare_dataset(_: Dict[str, Any] | None = None) -> Dict[str, Any]:
    # Conceptually a goal node; returns a "context" dict for downstream tasks.
    return {"dataset_path": "data.csv"}

def load_data(ctx: Dict[str, Any]) -> Dict[str, Any]:
    # Pretend we loaded a dataset
    return {"rows": 100, "columns": 5, "missing_values": 12, **ctx}

def validate_schema(data: Dict[str, Any]) -> Dict[str, Any]:
    # Pretend schema is valid; attach validation result
    return {**data, "schema_valid": True}

def clean_missing(data: Dict[str, Any]) -> Dict[str, Any]:
    # Pretend we cleaned missing values and reduced rows slightly
    cleaned_rows = data["rows"] - 5
    return {**data, "rows": cleaned_rows, "missing_values": 0}

def compute_features(data: Dict[str, Any]) -> Dict[str, Any]:
    # Pretend we computed features
    return {**data, "features": ["f1", "f2", "f3"]}

# Registry mapping task name -> function
TASKS = {
    "prepare_dataset": prepare_dataset,
    "load_data": load_data,
    "validate_schema": validate_schema,
    "clean_missing": clean_missing,
    "compute_features": compute_features,
}
```

Key idea:

* Each task returns a dict artifact (like a dataset state).
* Downstream tasks receive that artifact as input.
* This makes caching meaningful: you cache the artifact for each step.

---

### ✅ Your step now

Create `tasks.py` with the above.

When done, say **“Step 3 done”** and we’ll implement BFS planning + DFS execution with caching in `agent.py`.

Awesome — now we build the “agent brain”: planning (BFS) + execution (DFS-style dependency resolution) + caching.

---

## ✅ Step 4 — Planning + Execution (`agent.py`)

Copy/paste the following into `agent.py`:

```python
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
    Execute tasks using DFS-style dependency resolution + memoization.

    Returns: dict mapping task_name -> task_output_artifact
    """

    results: Dict[str, Dict[str, Any]] = {}

    def run(task_name: str) -> Dict[str, Any]:
        # 1) Memoization: reuse task output if already computed
        if cache.has(task_name):
            return cache.get(task_name)  # type: ignore[return-value]

        # 2) Resolve dependencies first (DFS)
        deps = graph.get(task_name, [])
        dep_artifact: Dict[str, Any] | None = None

        # If there are dependencies, run them in order and pass the most recent artifact forward.
        # (Simple but realistic: each step refines the same "dataset artifact".)
        for dep in deps:
            dep_artifact = run(dep)

        # 3) Execute the task itself
        if task_name not in tasks:
            raise KeyError(f"No task function registered for '{task_name}'")

        fn = tasks[task_name]

        # Root task may accept None; others take the artifact
        if dep_artifact is None:
            output = fn(None)
        else:
            output = fn(dep_artifact)

        # 4) Store in cache and results
        cache.set(task_name, output)
        results[task_name] = output
        return output

    # Important: We execute starting at the root goal node
    run(start)
    return results
```

### What’s happening here

* `plan_bfs()` gives a **planner’s view** of the workflow.
* `execute_with_cache()` does **dependency-first execution** (DFS-ish), caching results so repeated calls don’t re-run.

---

### ✅ Your step now

Create `agent.py` with the above.

Then say **“Step 4 done”** and we’ll do Step 5: run it and interpret output + add a tiny “cache hit” demonstration.

Perfect — now we’ll run the capstone and then make caching *visible* (so you can literally see DP in action).

---

# ✅ Step 5 — Run the Project Once (Baseline)

From inside `module_1_capstone/`, run:

```bash
python main.py
```

### What you should see (roughly)

* A BFS “Execution plan” list
* Then results for each task (dict outputs)

**Important note:** The BFS plan is a traversal order, not necessarily a strict dependency-validated schedule (we’ll tighten this later in Module 10 with real orchestration/topological sorts). For this capstone, it’s perfect for intuition.

---

## 🔍 Step 5a — Make Cache Hits Visible (Small Edit)

Right now caching is happening, but you don’t *see* it. Let’s add one print so it becomes obvious.

In `agent.py`, inside `run(task_name: str)` replace:

```python
if cache.has(task_name):
    return cache.get(task_name)
```

with:

```python
if cache.has(task_name):
    print(f"[CACHE HIT] {task_name}")
    return cache.get(task_name)  # type: ignore[return-value]
```

---

### 🔁 Step 5b — Trigger Cache Hits (Small Edit in `main.py`)

In `main.py`, after the first execution, add a second execution using the *same* cache:

Find this line:

```python
results = execute_with_cache(task_graph, TASKS, start="prepare_dataset", cache=cache)
```

Immediately after it, add:

```python
print("\n=== Execution Again (should hit cache) ===")
results2 = execute_with_cache(task_graph, TASKS, start="prepare_dataset", cache=cache)
```

You don’t need to print `results2` — the cache hit messages will prove it’s working.

---

### ✅ Your step now

1. Run `python main.py`
2. Apply the two small edits (cache hit print + second execution)
3. Run it again
4. Paste your console output here

Once I see your output, we’ll do **Step 6 (final polish)**:

* clarify “dependencies” vs “children” naming
* make the execution order explicit (and return it)
* add a lightweight “task signature” cache key option (realistic upgrade)


Nice — this is working end-to-end, and you just proved caching is functioning. ✅

Two quick observations (both are “capstone polish” and will make the caching strategy feel more realistic):

1. You only see a cache hit for `prepare_dataset` because the second run stops immediately at the root due to the cache check.
2. In real pipelines/agents, you usually want either:

   * **cache hits per-node** (still traverse but reuse results), or
   * **cache keys that include inputs** (so cached values stay valid when inputs change)

Let’s do a light Step 6 polish that addresses both while keeping the project simple.

---

## ✅ Step 6 — Final Polish

### 6.1 Traverse the whole DAG on rerun (show cache hits for every task)

In `agent.py`, inside `run(...)`, change the cache block from “return immediately” to “reuse but still traverse children”.

Replace:

```python
if cache.has(task_name):
    print(f"[CACHE HIT] {task_name}")
    return cache.get(task_name)
```

with:

```python
if cache.has(task_name):
    print(f"[CACHE HIT] {task_name}")
    output = cache.get(task_name)  # type: ignore[assignment]
    # Still traverse children so you can see cache hits downstream too
    for child in graph.get(task_name, []):
        run(child, output)
    return output  # type: ignore[return-value]
```

**What this changes:**
On the second execution, you should now see cache hits for:
`prepare_dataset`, `load_data`, `validate_schema`, `clean_missing`, `compute_features`.

---

### 6.2 Make caching slightly more realistic: key on (task_name + dataset_path)

Right now, the cache key is just the task name. That’s OK for learning, but in practice you’d key by “task + inputs”.

A super-simple realistic key here is:

* `dataset_path` (because it uniquely identifies the dataset in this toy pipeline)

Update `cache.py` to accept any hashable key (it already does), and then in `agent.py` compute a key like:

```python
cache_key = f"{task_name}:{artifact_in.get('dataset_path', 'none')}" if artifact_in else f"{task_name}:none"
```

#### Minimal change (recommended)

In `agent.py`, inside `run(...)`, add this near the top:

```python
cache_key = (
    f"{task_name}:{artifact_in.get('dataset_path', 'none')}"
    if artifact_in is not None else
    f"{task_name}:none"
)
```

Then replace every `cache.has(task_name)` / `cache.get(task_name)` / `cache.set(task_name, ...)` with the `cache_key` version:

```python
if cache.has(cache_key):
    ...
    output = cache.get(cache_key)
    ...
cache.set(cache_key, output)
```

**Why this matters:**
If later you change `prepare_dataset` to return a different dataset path (say `"data_v2.csv"`), the cache won’t incorrectly reuse results from `"data.csv"`.

---

### 6.3 Tiny “stakeholder-friendly” summary

In `main.py`, after printing results, add:

```python
print("\n=== Summary ===")
print(f"Planned {len(plan)} tasks. Executed {len(results)} tasks.")
```

This is the kind of line that makes sprint demos feel crisp.

---

## ✅ What to do now

1. Apply **6.1** first (fastest, immediate payoff)
2. Run `python main.py` and paste the output (you should see all cache hits)
3. Then apply **6.2** (input-aware cache key) and run again
4. (Optional) apply **6.3**

Once you paste the “all cache hits” output, I’ll help you do a quick final wrap-up writeup for the capstone (what you built + how it maps to Module 1 concepts).

# Appendix

Yep — your mental model is on point, and you’re asking exactly the “architecture” question that separates toy agents from production ones.

### The short answer

**In small systems (like our capstone), it’s totally normal to keep planning + execution in `agent.py`.**
**In larger/at-scale systems, you usually *separate* them into modules/classes**, but you still keep them under the “agent layer” (or “orchestrator layer”) because that layer owns *control flow*.

---

## 1) Where BFS/DFS “live” conceptually

Think in layers:

* **Graph / State representation** (what exists): `task_graph`, nodes/edges
* **Planning logic** (decide what to do): BFS-like (or other planners)
* **Execution logic** (do it): DFS-like dependency resolution / traversal
* **Caching / memory** (don’t repeat work): memoization, artifact stores
* **Tools** (actual work): loading data, cleaning, summarizing, etc.

In our capstone:

* `tasks.py` = tools
* `agent.py` = planning + execution + caching (control plane)
* `main.py` = entry point

That’s a clean “agent orchestrator owns control flow” model.

---

## 2) Is it common to define BFS/DFS in `agent.py`?

### ✅ In prototypes and “single-agent” systems: yes

It’s very common to see:

* `agent.py` (or `orchestrator.py`) contains:

  * plan generation
  * task routing
  * tool calling
  * caching hooks
  * retries / error policies

Because the agent’s job is to coordinate.

### ✅ In production: it depends on scale, but it’s still the right *layer*

At scale, you’ll rarely have raw functions named `plan_bfs()` and `execute_dfs()` sitting directly in `agent.py`, but the *concept* still belongs there.

Instead you’ll see patterns like:

* `planner.py` (planning policy)
* `executor.py` (execution engine)
* `memory.py` (cache + artifact store)
* `agent.py` (wires them together)

So: **planning/execution still “live” in the agent layer**, even if the code is split across files.

---

## 3) Why it’s OK that planning sits next to execution (even at scale)

Your Module 0 recollection is correct:

> `agent.py` is orchestration.

And orchestration inherently includes **both**:

* *choosing a plan* (planning)
* *running the plan* (execution)

A useful analogy:

* “planner” produces a route
* “executor” drives the car
* “agent/orchestrator” is the thing that:

  * asks for a route
  * decides whether to reroute
  * drives
  * stops for gas
  * records where it’s been (memory)

So it’s not weird that `agent.py` touches both — it’s natural.

---

## 4) The “real” distinction: policy vs mechanism

This is the key architectural refinement.

### Policy (what to do)

* BFS vs DFS
* heuristics
* scoring
* priority rules
* constraints

### Mechanism (how to do it)

* queue/stack
* retries
* concurrency
* caching implementation
* tool adapters

In production, you often separate:

* **Planner policy** (which may *use* BFS)
  from
* **Execution mechanism** (which may *use* DFS)

But the agent/orchestrator still owns assembling them.

---

## 5) Your caching intuition is correct

You said:

> it makes sense caching logic would live alongside where DFS logic is defined

✅ Exactly.

Because caching is most effective when it’s closest to the place where repeated subproblems happen. In our capstone, repeated work happens in execution traversal, so caching sits in the execution loop.

At scale, you might move caching behind an interface (e.g., `ArtifactStore`, `ResultCache`), but it still integrates tightly with execution.

---

## 6) What “at-scale multimodal agentic systems” usually do

A realistic structure you’ll commonly see is:

```
agent/
  agent.py          # orchestration + wiring
  planner.py        # plan generation (BFS/beam/heuristics)
  executor.py       # task runner (DFS / topo order / async)
  memory.py         # caches, stores, vector DB hooks
tools/
  io_tools.py
  vision_tools.py
  stats_tools.py
models/
  schemas.py
```

So:

* BFS/DFS-like logic is still **in the agent layer**
* but split into components for maintainability and testing

---

## 7) Why our capstone merged them (and why that’s good)

We merged them in `agent.py` because:

* it keeps the mental model tight
* it reduces moving parts while learning
* it makes the connection between Module 1 concepts explicit
* it’s easier to debug

Then later modules (especially orchestration / tools / concurrency) will motivate splitting them.

---

## Practical takeaway

**Yes**, planning and execution commonly sit “together” at the agent/orchestrator layer.
**No**, they don’t always sit in the same file in production — they’re often separated into planner/executor modules — but they remain part of the same *control plane* owned by the agent.

---

If you want, before we do the post-capstone reflection, I can show you a *tiny refactor* (no behavior change) that splits:

* `planner.py` (BFS planning)
* `executor.py` (DFS + cache execution)
* `agent.py` (wiring)

That would make the “at-scale” pattern extremely concrete without adding complexity.
