**Python Code**
```python
import pprint

# Prepare dataset
task_graph = {
    'load_csv': [ 'validate_schema', 'clean_missing_values' ],
    'validate_schema': [],
    'clean_missing_values': ['compute_features'],
    'compute_features': []
}

print(task_graph)
```

**Console Output**
```
(.venv) C:\Projects\cs_foundations_for_agentic_multimodal_ai>python C:\Projects\cs_foundations_for_agentic_multimodal_ai\module_1\exercises\exercise_1_2\e1_2_answer.py
{'load_csv': ['validate_schema', 'clean_missing_values'], 'validate_schema': [], 'clean_missing_values': ['compute_features'], 'compute_features': []}
```