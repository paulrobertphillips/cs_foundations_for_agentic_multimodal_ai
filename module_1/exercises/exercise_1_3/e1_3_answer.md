**Python Code**
```python
from collections import deque

task_graph = {
    'prepare_dataset': ['load_csv'],
    'load_csv': [ 'validate_schema', 'clean_missing_values' ],
    'validate_schema': [],
    'clean_missing_values': ['compute_features'],
    'compute_features': []
}

### BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft() # FIFO

        if node not in visited:
            print("Visited:", node)
            visited.add(node)

            # Enqueue all neighbors
            # E.g., checking for dependencies of current node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor) # visit immediate dependency next

print('BFS Example')
print(bfs(task_graph, 'prepare_dataset'))

### DFS

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop() # LIFO

        if node not in visited:
            print('Visiting:', node)
            visited.add(node)
            stack.extend(graph[node])

print('DFS Example')
print(dfs(task_graph, 'prepare_dataset'))
```

**Console Output**
```
(.venv) C:\Projects\cs_foundations_for_agentic_multimodal_ai>python C:\Projects\cs_foundations_for_agentic_multimodal_ai\module_1\exercises\exercise_1_3\e1_3_answer.py
BFS Example
Visited: prepare_dataset
Visited: load_csv
Visited: validate_schema
Visited: clean_missing_values
Visited: compute_features
None
DFS Example
Visiting: prepare_dataset
Visiting: load_csv
Visiting: clean_missing_values
Visiting: compute_features
Visiting: validate_schema
None
```