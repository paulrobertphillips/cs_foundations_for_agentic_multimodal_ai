````markdown

**main.py**
```python
from tools.io_tools import load_numbers
from tools.stats_tools import compute_stats

numbers = load_numbers("numbers.json")
print(compute_stats(numbers))
```


**tools/io_tools.py**
```python
import json
def load_numbers(path):
    with open(path) as f:
        return json.load(f)
```

**tools/stats_tools.py**
```python
import math
def compute_stats(numbers):
    return {"mean": sum(numbers)/len(numbers)}
```
