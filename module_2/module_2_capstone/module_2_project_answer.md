## Phase 1 - Safe Refactor

**Step 1A - Refactor Planning Prompt (No Code)**
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

Propose a plan for this sprint slice only.
No code. Wait for approval.
```

**Step 1B - Refactor Execution Prompt**
```
Using the approved refactor plan:

Apply the refactor exactly as described.

Constraints:
 - Python 3.10
 - pandas only
 - No new dependencies
 - No refactors outside this slice
 - Preserve all existing behavior
 - Keep all public interfaces identical
 - No new abstractions
 - Do not modify existing tests

Deliverable:
Code diff and test results only.
```

## Phase 2

**AI Review Report Prompt**
```
You are acting as a constrained code reviewer.

Review type:
Safe refactor (behavior-preserving)

Scope reviewed:
- Data ingestion module
- Schema validation logic

Out-of-scope:
- Data cleaning
- Feature engineering
- Modeling
- Performance optimization

Inputs reviewed:
- Code files:
  - tasks.py
  - executor.py
  - agent.py
  - main.py
- Tests:
  - tests/test_tasks.py
- Reference artifacts:
  - Approved refactor plan
  - Sprint acceptance criteria

Review checks to perform:
- Scope adherence
- Behavior preservation
- Public interface stability
- Test coverage
- Risk assessment

Instructions:
1) Generate an AI Review Report using the provided checklist structure
2) Reference specific files/functions where relevant
3) Clearly distinguish confirmed facts from assumptions
4) Explicitly state review limitations
5) Do NOT propose refactors or improvements
6) Do NOT rewrite code

Deliverable:
A completed AI Review Report in Markdown format only.
```

## Phase 3 - Human-Facing Summaries

**Review Checklist Summary**
```
 - Code for project's data ingestion & schema validation step was refactored to improve readability & maintainability.
 - Review outcome of refactoring showed that no functional or architectural changes were made.
 - All tests passed unchanged.
 - Risk is low, no downstream consumers were impacted.
```

**Stakeholder Update**
```
This sprint focused on improving the maintainability of the data ingestion step. Review confirmed no functional behavior changed. All existing tests passed unchanged. Implementation risk is low, no downstream dependencies were impacted.
```

