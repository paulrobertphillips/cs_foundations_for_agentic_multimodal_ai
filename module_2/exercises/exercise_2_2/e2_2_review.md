This is a solid submission — you’re doing the most important thing in Module 2.2: **explicit mode separation** (“PLANNING ONLY” vs “EXECUTION ONLY”). That alone prevents a ton of drift.

A few targeted notes to make these prompts even more “production-safe” (and consistent with your agile + stakeholder-trust goals).

---

## Planning Prompt Review

### What’s great ✅

* **Role** is clear (“junior data engineer”)
* **No-code constraint** is explicit
* You request **assumptions**
* You request **in-scope vs out-of-scope**
* “Stop after the plan and wait for approval” is perfect

### Two small improvements (optional but high ROI)

1. **Explicit deliverable format**
   Add something like:

   * “Return a numbered list with: Step name / Inputs / Outputs / Failure modes (1 sentence).”
     This forces the plan to be reviewable and sets up stable interfaces.

2. **Clarifying questions placement**
   Right now you say “Ask clarifying questions if ambiguous,” but you also say “Stop after the plan.”
   Minor conflict. Better is:

   * “If anything is ambiguous, list questions at the end under ‘Open Questions’.”

**Tightened version:**

```text
Return:
1) Numbered pipeline steps (step name + 1–2 sentence description)
2) For each step: input artifact, output artifact (brief)
3) Assumptions
4) In-scope vs out-of-scope for Iteration 1
5) Open questions (if any)
No code. Stop after the plan.
```

---

## Execution Prompt Review

### What’s great ✅

* References “previously approved plan” (critical)
* Limits scope to **two steps**
* Forbids architecture changes
* Specifies `pandas` and “modular, testable functions”
* “python code only” is a strong output constraint

### Three fixes/tweaks to prevent common AI failure modes

1. **Spell “Deliverable” correctly**
   AI usually handles typos fine, but it’s worth fixing:

   * `Delivarable` → `Deliverable`

2. **Make inputs/outputs explicit**
   Otherwise the AI may invent a class, a pipeline framework, or hidden globals.
   Add:

   * `load_data(path: str) -> pd.DataFrame`
   * `validate_schema(df: pd.DataFrame, required_columns: list[str]) -> None | raise ValueError`

3. **Add “no extra dependencies”**
   Otherwise it may import pydantic, great-expectations, pandera, etc.
   Add:

   * “pandas only; standard library allowed; no new third-party libraries.”

**Tightened version:**

```text
Using the previously approved plan:

EXECUTION ONLY — do not change scope or architecture.

Implement ONLY:
1) load_data(path: str) -> pandas.DataFrame
2) validate_schema(df: pandas.DataFrame, required_columns: list[str]) -> None
   - raise ValueError with a clear message if validation fails

Constraints:
- Python 3.10
- pandas only (+ standard library)
- No additional third-party dependencies
- No classes/frameworks; just functions
- Include minimal docstrings and type hints

Deliverable:
Python code only.
```

---

## Small note: your code fences say `haskell`

Doesn’t matter for meaning, but for readability you may want `text` or just plain triple backticks. Not required — just cleaner.

---

## Quick “drift risk” check (what AI might still do)

Even with your prompts, AI sometimes:

* adds extra steps in execution (“since you’ll need cleaning…”)
* returns markdown + explanations despite “code only”
* introduces a config object or class

Your constraints already reduce this a lot; the “no extra deps / no architecture changes / code only” combo is the right defense.

---

# ✅ Module 2.2 complete

You now have a reusable pattern:

* **Prompt A:** plan-only, assumptions, scope, stop
* **Prompt B:** execute-only, limited scope, stable interfaces, code-only

This is the backbone of AI-assisted agile development.

---

If you’re ready, we’ll move to:
