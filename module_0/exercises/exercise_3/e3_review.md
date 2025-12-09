Great work — you’re very close! Your structure is correct, and you clearly understand how dataclasses are meant to be used.
There are just **two tiny syntax issues** to fix:

---

### ✅ **1. You need to import `dataclass`**

At the top of the file, add:

```python
from dataclasses import dataclass
```

---

### ✅ **2. Your class definition is missing a colon (`:`)**

Python requires:

```python
class ExperimentConfig:
```

…but your version is:

```python
class ExperimentConfig
```

So let’s fix that.

---

### ⭐ **Corrected Full Answer**

```python
from dataclasses import dataclass

@dataclass
class ExperimentConfig:
    dataset_name: str
    learning_rate: float
    epochs: int = 10
    use_gpu: bool = False


cfg = ExperimentConfig(dataset_name="materials_v1", learning_rate=0.001)
print(cfg)
```

---

### 🎉 **What the output will look like**

```
ExperimentConfig(dataset_name='materials_v1', learning_rate=0.001, epochs=10, use_gpu=False)
```

This confirms:

* the dataclass auto-generated `__repr__`
* default field values work
* annotations were parsed correctly

You nailed the conceptual part — just minor syntax polish.

---

### ⭐ Ready for Module 0.4?

Now that you understand dataclasses, you're ready to learn:

* **Type hints** (why static typing matters for AI tooling)
* **Pydantic** models (how agent frameworks validate inputs/outputs)
* How dataclasses and Pydantic complement each other
* When to use which

Would you like to proceed to **Module 0.4**?
