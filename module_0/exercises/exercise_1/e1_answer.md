**folder structure**
```
my_project/
    main.py
    tools/
        __init__.py
        io_tools.py
    processing/
        __init__.py
        data_tools.py
```

**tools/io_tools.py**
```python
import csv

def read_csv(path):
    with open(path) as f:
        """Return contents of opened CSV file as list."""
        return list(csv.DictReader(f)) 
```

**processing/data_tools.py**
```python
def filter_rows(rows):
    """Return only rows where 'value' > 10."""
    return [r for r in rows if float(r["value"]) > 10]
```

**main.py**
```python
from tools.io_tools import read_csv
from processing.data_tools import filter_rows

rows = read_csv("data.csv")
print(filter_rows(rows))
```


