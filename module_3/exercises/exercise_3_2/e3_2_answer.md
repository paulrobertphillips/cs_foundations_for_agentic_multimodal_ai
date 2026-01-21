### Ticket 1

Sprint goal:
Remove outliers from dataset based on column `energy consumption`.

In scope:
- Identify outlier values in `energy consumption`
- Remove records containing outliers

Out of scope:
- Feature scaling
- Imputation
- Model training

Acceptance criteria:
- Output DataFrame has no outlier `energy consumption` values
- Outliers are computed only from training data
- Existing tests pass unchanged

### Ticket 2

Sprint goal:
Refactor the data ingestion function used for the `energy price` data source to improve maintainability and reduce duplication, no behavior change.

In scope:
- Reduce duplication
- Improve naming and docstrings
- Extract helper functions where it reduces complexity
- Add type hints where they clarify interfaces
- Keep the current module/file structure unless a move is purely organizational
- Confirm that all existing callers of functions will continue to work unchanged

Out of scope:
- Any changes to runtime behavior
- Any changes to public function signatures
- Introducing classes/frameworks (functions only)
- Adding new third-party dependencies
- Performance optimizations unless measured and approved

Acceptance criteria:
- All existing tests pass unchanged
- Public function signatures remain identical
- Outputs for the same inputs are unchanged (behavior-preserving)

### Ticket 3

Sprint goal:
Set random seeds and fix train/validation splits for the model training function to improve reproducibility.

In scope:
- Setting random seeds
- Fix train/validation splits

Out of scope:
- Replacing existing modeling approach
- Model evaluation

Acceptance criteria:
- Model training function has random seeds implemented
- Train/validation splits in model training function have been fixed