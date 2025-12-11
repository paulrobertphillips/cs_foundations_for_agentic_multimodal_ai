**Python Code**
```python
import pprint

def all_pairs(seq):
    pairs = []
    for a in seq:
        for b in seq:
            pairs.append((a,b))
    
    return pairs

actions = ["A", "B", "C"]

results = all_pairs(actions)

# Print individual sequences
pprint.pprint(results)

# Print total count of unique sequences
print('\nTotal Count: '+str(len(results)))
```

**Console Output**
```
(.venv) C:\Projects\cs_foundations_for_agentic_multimodal_ai\module_0\project_root>python C:\Projects\cs_foundations_for_agentic_multimodal_ai\module_1\exercises\exercise_1_1\e1_1_answer.py
[('A', 'A'),
 ('A', 'B'),
 ('A', 'C'),
 ('B', 'A'),
 ('B', 'B'),
 ('B', 'C'),
 ('C', 'A'),
 ('C', 'B'),
 ('C', 'C')]

Total Count: 9
```