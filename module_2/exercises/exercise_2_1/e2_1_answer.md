**Original Prompt**
```
Create a Python solution to analyze a dataset.
```

**Rewritten Structured Prompt**
```
You are acting as a junior data engineer.

Goal:
We are building a reproducible data science pipeline that will eventually include:
 - data ingestion
 - schema validation
 - data cleaning
 - exploratory data analysis

Do NOT implement the full pipeline yet.

Non-goals (out of scope for this step):
- Feature engineering
- Modeling
- Visualization
- Performance optimization

Constraints:
 - Python 3.10
 - pandas only
 - Modular functions
 - Deterministic behavior
 - Code should be easy to extend later

Plan first:
1) Propose a high-level pipeline outline for the *full* workflow (steps only)
2) Clearly mark which steps are IN SCOPE vs OUT OF SCOPE
3) Wait for approval before writing any code

Deliverable:
 - A short written plan
 - Then, after approval, Python functions for data loading and schema validation only

Design note:
Assume downstream steps will consume the outputs of these functions, so return values should be structured and explicit.
```