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
bfs(task_graph, 'prepare_dataset')

### DFS

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  # LIFO
        
        if node not in visited:
            print('Visiting:', node)
            visited.add(node)
            stack.extend(graph[node])

print('DFS Example')
dfs(task_graph, 'prepare_dataset')



