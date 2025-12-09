
**Define `ExperimentConfig`**
```python
from dataclasses import dataclass

@dataclass
class ExperimentConfig:
    dataset_name: str
    learning_rate: float
    epochs: int = 10
    use_gpu: bool = False
```

**Instantiate `ExperimentConfig`**
```python
cfg = ExperimentConfig(dataset_name="materials_v1", learning_rate=0.001)
print(cfg)
```


