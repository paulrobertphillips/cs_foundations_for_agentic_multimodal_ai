Great — let’s jump into the **Module 0.5 async mini-exercise**.
This will give you hands-on experience with:

* `async` / `await`
* scheduling concurrent tasks
* using `asyncio.gather`
* seeing the time savings of concurrency

Exactly the kind of async flow used in agent frameworks for parallel tool calls.

---

### 🧪 **Module 0.5 — Async Mini-Exercise**

**Goal**

Simulate running 3 experiments of different durations **concurrently** using `asyncio`.

This parallels how an agent might run:

* multiple model queries
* several data fetches
* multiple long-running tasks

at the same time.

---

### ✅ **Exercise Requirements**

**Step 1 — Define an async function**

Create:

```python
import asyncio

async def run_experiment(name: str, seconds: int):
    print(f"[{name}] starting...")
    await asyncio.sleep(seconds)
    print(f"[{name}] finished after {seconds} seconds")
    return name, seconds
```

This simulates a slow operation.

---

### **Step 2 — Run all experiments concurrently**

**Create an `async main()` function:**

```python
async def main():
    tasks = [
        run_experiment("exp_small", 1),
        run_experiment("exp_medium", 2),
        run_experiment("exp_large", 3),
    ]
    results = await asyncio.gather(*tasks)
    print("All done:", results)
```

---

### **Step 3 — Execute the async event loop**

**At the bottom of the file:**

```python
asyncio.run(main())
```

---

### ⭐ What you should observe

Expected console output (order may vary slightly):

```
[exp_small] starting...
[exp_medium] starting...
[exp_large] starting...
[exp_small] finished after 1 seconds
[exp_medium] finished after 2 seconds
[exp_large] finished after 3 seconds
All done: [('exp_small', 1), ('exp_medium', 2), ('exp_large', 3)]
```

### Key Insight

Even though total sleep time is:
1 + 2 + 3 = **6 seconds**

The async version finishes in **~3 seconds**, the time of the longest task.

This is how **agentic parallelism at the I/O level** works.

---

### 🎯 **Your Task Now**

Reply back with:

1. **Your code** (same Markdown/code block format as previous exercises)
2. **The console output** you observed

I’ll verify correctness and then we’ll finish Module 0 with:

**→ The real-world async pattern used by AI agents (async tool calls)**
**→ A preview of Module 1 (algorithmic thinking for agent planning)**

Excited to see your implementation!
