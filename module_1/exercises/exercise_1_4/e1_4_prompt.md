# 🧪 **Module 1.4 — Mini-Exercise: Recursive Traversal of a Reasoning Tree**

This exercise focuses on **hierarchical structure** and **subproblem decomposition** using recursion.

No BFS or queues here — this is **pure DFS via recursion**.

---

## 🧠 **Concept Recap (Very Short)**

* A **reasoning tree** represents a problem broken into subproblems
* Each node has:

  * a value (the task or idea)
  * zero or more child nodes
* Recursion is a natural way to traverse this structure

---

## 📋 **Tree Structure to Use**

Use the following reasoning tree **exactly as given**:

```python
reasoning_tree = (
    "root",
    [
        ("idea1", []),
        ("idea2", [
            ("idea2a", [])
        ])
    ]
)
```

This represents:

```
root
 ├─ idea1
 └─ idea2
      └─ idea2a
```

---

## 🎯 **Your Task**

Write a **recursive function** that:

1. Takes a node of the tree as input
2. Prints the node’s value
3. Recursively visits each child

### Requirements

* Use recursion (no stacks, no queues)
* Print each node exactly once
* Print in **depth-first order**
* Keep the function simple and readable

---

## 🧪 **Submission Format**

Please reply with:


**Python Code**
```python
...
```

**Console Output**

```
...
```

---

## 🔍 **What You Should Observe**

- The traversal order mirrors DFS
- The call stack replaces the explicit stack
- Each recursive call handles a *subproblem*
- The code stays short and expressive

This is the same pattern used for:
- reasoning trees
- nested workflows
- backtracking logic
- agent reflection loops

---

## 🧠 **Why This Matters for Agents**

Agents frequently:
- break tasks into subtasks
- reason hierarchically
- explore ideas deeply
- backtrack when needed

Recursion is the clearest way to express that behavior.

---

When you’re ready, send your recursive solution — and after that we’ll move to **Module 1.5 (Dynamic Programming & Memoization)**, where we learn how to *optimize* recursive reasoning.

