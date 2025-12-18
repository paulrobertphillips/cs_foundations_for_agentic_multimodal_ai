**Refactor Planning Prompt**
```
You are acting as a junior engineer.

Sprint goal:
Refactor the existing ingestion + schema validation code to improve readability and maintainability, without changing behavior.

Context (future work, not now):
This pipeline will later expand to cleaning, feature engineering, and model training.

In scope (this sprint):
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
 - Refactor plan lists exact files/functions to change
 - Refactor plan explains why each change improves maintainability

Task (PLANNING ONLY):
 1) Propose a refactor plan (no code)
 2) List exact changes by file/function
 3) State explicitly what will NOT change
 4) Identify the highest-risk change (if any) and how to mitigate it

Stop after the plan and wait for approval.
```

**Refactor Execution Prompt**
```
Using the approved refactor plan:

Apply the refactor exactly as described.

Constraints:
 - Preserve all existing behavior
 - Keep all public interfaces identical
 - No new abstractions
 - Do not modify existing tests

Deliverable:
Code diff only.
```