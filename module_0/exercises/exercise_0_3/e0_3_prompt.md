# Module 0.3 — Dataclasses

### 🧪 Want to try the Module 0.3 mini-exercise?

Here’s your task:

**Create a dataclass named `ExperimentConfig` with fields:**
 - `dataset_name` (str)
 - `learning_rate` (float)
 - `epochs` (int) — default 10
 - `use_gpu` (bool) — default False

**And then instantiate it:**

```
cfg = ExperimentConfig(dataset_name="materials_v1", learning_rate=0.001)
print(cfg)
```

Use a code block format like before if you want me to check it.