import pprint

# Prepare dataset
task_graph = {
    'load_csv': [ 'validate_schema', 'clean_missing_values' ],
    'validate_schema': [],
    'clean_missing_values': ['compute_features'],
    'compute_features': []
}

print(task_graph)

