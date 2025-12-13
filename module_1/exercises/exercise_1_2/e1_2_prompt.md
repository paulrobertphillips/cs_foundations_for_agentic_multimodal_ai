# 🧪 **Module 1.2 — Mini-Exercise: Representing a Task Graph**

This exercise is about translating a **conceptual workflow** into a **graph data structure**.
No traversal yet — just *representation*.

---

## 🎯 **Goal of the Exercise**

You will represent a **data science workflow** as a **directed graph** using a Python dictionary.

This is exactly how:

* DAG schedulers (Airflow, Prefect)
* agent planners
* workflow engines

internally model pipelines.

---

## 🧠 **Concept Refresher (Very Short)**

* **Nodes** → tasks
* **Edges** → “must happen before”
* **Graph** → `dict[str, list[str]]`
* **Directed** → parent → children
* **Leaves** → empty list

---

## 📋 **Workflow to Model**

You are given this conceptual workflow:

```
Prepare Dataset
 ├─ Load CSV
 │   └─ Validate Schema
 ├─ Clean Missing Values
 └─ Compute Features
```

---

## 🧩 **Your Task**

Create a Python dictionary where:

* each **key** is a task name (node)
* each **value** is a list of tasks that depend on it (edges)

### ✅ Requirements

* Use clear, readable task names (snake_case is fine)
* All tasks must appear as keys
* Leaf nodes must map to an empty list
* This must be a **directed graph**

---

## 📌 **Expected Structure (Conceptual, Not Code)**

You should end up with something like:

```
task → [dependent_task_1, dependent_task_2]
```

But **do not copy this** — implement it yourself.

---

## 🧪 **What to Submit**

Please reply with:

1. **Your Python dictionary**
2. (Optional but encouraged) A pretty-printed version using `pprint`

Example submission format (same style you’ve been using):

**Python Code**
```python
...
```

**Console Output**
```
...
```

---

## 🔍 **Why This Matters for Agents**

This is the *exact* structure an agent would:

- reason over
- traverse with BFS/DFS
- convert into an execution plan
- parallelize where possible
- validate dependencies

In later exercises, this graph will become **input to an agent**.

---

When you’re ready, send your solution — and after that we’ll move naturally into:
- **Module 1.3 — BFS & DFS traversal**, using *this exact graph*.
