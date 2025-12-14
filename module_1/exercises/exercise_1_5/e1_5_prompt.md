# 🧪 Module 1.5 — Mini-Exercise: Memoization (Dynamic Programming)

## ✅ Concept

Write a function:

```python
count_paths(n)
```

that returns the number of ways to climb a staircase of `n` steps if you can take **1 step** or **2 steps** at a time.

### Expected values

* `count_paths(1) = 1`
* `count_paths(2) = 2`
* `count_paths(3) = 3`
* `count_paths(4) = 5`
* `count_paths(5) = 8`

This is the classic “staircase” recurrence:

```
count_paths(n) = count_paths(n-1) + count_paths(n-2)
```

---

## 🎯 Your Task

### Requirements

* Use **recursion**
* Use **memoization** with a dictionary (cache)
* Keep it readable and well-commented
* Demonstrate it works by printing results for `n=1..6` (or at least `n=5`)

---

## 📌 Starter Template (Optional)

You can use this template if helpful:

```python
def count_paths(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    # base cases here

    # recursive case here
    memo[n] = ...
    return memo[n]
```

---

## 🧠 Why this matters for agents

This mirrors agent reasoning where the agent repeatedly reaches the *same subproblem state*. Memoization prevents repeated work and makes deep exploration feasible.

---

## ✅ What to Submit

Same format as before:

* **Python Code**
* **Console Output**

When you post your solution, I’ll review it and then we’ll transition into the **Module 1 Capstone** where we’ll add a practical caching layer (e.g., caching “tool results” or “planned steps”) so you can see this idea in a real workflow.

Go ahead and send your implementation when ready.

# Appendix

## 1️⃣ What “base cases” actually mean (plain language)

In recursion, a **base case** is:

> A situation where the answer is known immediately and no further recursion is needed.

Think of base cases as:

* the **stopping conditions**
* the **smallest solvable subproblems**
* the **anchors** that prevent infinite recursion

Without base cases, recursion never ends.

---

## 2️⃣ What are the base cases for `count_paths(n)`?

Recall the problem:

> Number of ways to climb `n` steps if you can take 1 or 2 at a time.

Let’s reason *without code*.

### If `n = 1`

You have:

* 1 step → only one way: `[1]`

So:

```python
count_paths(1) = 1
```

---

### If `n = 2`

You have:

* `[1, 1]`
* `[2]`

So:

```python
count_paths(2) = 2
```

These are your **base cases** because:

* they don’t depend on smaller subproblems
* they are directly known

So in code:

```python
if n == 1:
    return 1
if n == 2:
    return 2
```

That’s it — nothing fancy.

---

## 3️⃣ What the recursive case *really* means

This is the most important conceptual step.

### Key idea

To reach step `n`, the **last move** must have been:

* a 1-step from `n-1`, or
* a 2-step from `n-2`

So the total number of ways to reach `n` is:

```
ways(n) = ways(n-1) + ways(n-2)
```

This is not arbitrary — it’s logical decomposition.

---

## 4️⃣ The correct recursive case (conceptually)

The recursive case is simply:

```python
count_paths(n-1) + count_paths(n-2)
```

And **then** we cache it:

```python
memo[n] = count_paths(n-1, memo) + count_paths(n-2, memo)
```

That’s the entire DP idea.

---

## 5️⃣ What this function is *actually doing* (agent perspective)

Think of this as an **agent solving subproblems**:

* “How many ways to reach step 5?”

  * “I need to know step 4 and step 3”
* “How many ways to reach step 4?”

  * “I need to know step 3 and step 2”
* “How many ways to reach step 3?”

  * “I need to know step 2 and step 1”

But once it figures out:

* `count_paths(3) = 3`

…it **never recomputes it again**.

That’s agent memory.

---

## 6️⃣ Why this is dynamic programming (not just recursion)

Without memoization:

* the same subproblems are recomputed repeatedly
* complexity is exponential

With memoization:

* each `n` is computed **once**
* complexity becomes linear

That’s the entire power of DP.

---

## 7️⃣ One-sentence takeaway (keep this)

> **Base cases are the smallest problems you can solve immediately; the recursive case breaks a problem into smaller versions of itself; memoization remembers those answers so you don’t repeat work.**

---
