Perfect — this “next-level” exercise is the one that most clearly shows **why Pydantic is so essential for AI agents**, because real systems pass around *nested*, structured data constantly.

Your task is:

1. Define a `Trial` model
2. Define an `Experiment` model that contains a list of `Trial` items
3. Instantiate the Experiment with **intentionally invalid nested values**
4. Observe how Pydantic catches errors deep inside the structure

Below is the **full exercise description**. You can copy/paste this into a file and fill it in.

---

### 🧪 **Nested Pydantic Exercise (Module 0.4 — Advanced)**

**Step 1 — Define the models**

```python
from pydantic import BaseModel

class Trial(BaseModel):
    id: int
    score: float


class Experiment(BaseModel):
    name: str
    trials: list[Trial]
```

This creates a two-level schema:
Experiment → List of Trial → Fields inside each trial

---

### **Step 2 — Instantiate with invalid nested data**

**Try constructing an experiment with these issues:**

* `"not an int"` instead of an integer for `id`
* `"NaN"` instead of a float for `score`
* This tests whether Pydantic validates inside the list structures

```python
exp = Experiment(
    name="test_experiment",
    trials=[
        {"id": "not an int", "score": "NaN"},
        {"id": 2, "score": 0.9}
    ]
)
```

Pydantic should throw a **nested ValidationError**, something like:

```
trials.0.id: value is not a valid integer
trials.0.score: value is not a valid float
```

This means:

* It correctly descended into the list
* It validated the *first* element
* It validated each field
* It preserved the structure in the error message

This is exactly how AI agents validate LLM-generated JSON or tool arguments.

---

### **Your task**

Please send:

1. Your code (as before, with code blocks)
2. The ValidationError traceback you receive

I’ll review it and confirm whether everything is working as expected.

When that’s done, we move to **Module 0.5 — Async Programming**, which is the final building block for scalable agent workflows.
