**Planning Prompt**
```haskell
You are acting as a junior data engineer.

Goal:
Design a data science pipeline for tabular CSV data.

Current task:
PLANNING ONLY - do not write any code.

Instructions:
 1) Propose a high-level pipeline outline (step names + brief descriptions)
 2) Identify assumptions about the data
 3) Clearly mark which steps are in scope vs out of scope for the first iteration
 4) Ask clarifying questions if anything is ambiguous

Stop after the plan and wait for approval.
```

**Execution Prompt**
```haskell
Using the previously approved plan:

Current task:
EXECUTION ONLY - do not change scope or architecture.

Instructions:
1) Implement the `load_data` and `validate_schema` steps only
2) Use pandas
3) Return modular, testable functions

Delivarable:
python code only
```