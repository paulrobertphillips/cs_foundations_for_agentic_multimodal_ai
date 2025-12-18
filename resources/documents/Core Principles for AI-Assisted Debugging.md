Great question — debugging is one of the **highest-leverage** places to use AI *well*, and also one of the easiest places for things to go wrong if prompts aren’t structured.

I’ll give you:

1. **Core best practices for AI-assisted debugging**
2. **A data-science debugging prompt (example)**
3. **An architecture / system-level debugging prompt (example)**
4. A short **anti-patterns checklist** (what to avoid)

No overlap with Module 3 governance — this is still firmly **Module 2: interaction mechanics**.

---

## 1️⃣ Core Principles for AI-Assisted Debugging (Memorize These)

### 🔑 Principle 1: Debugging ≠ Refactoring

When debugging, your goal is:

* **identify cause**
* **verify hypothesis**
* **apply minimal fix**

Not:

* “clean up”
* “improve design”
* “modernize code”

You must **explicitly forbid refactors** unless you *want* them.

---

### 🔑 Principle 2: Force Hypothesis Before Fix

AI is very good at proposing fixes.
AI is **less reliable** at identifying root causes unless forced.

So your prompt should always require:

1. probable cause(s)
2. evidence from code/logs
3. confirmation before changes

---

### 🔑 Principle 3: Minimize the Blast Radius

You should always constrain:

* files allowed to change
* functions allowed to change
* interfaces that must remain identical

This keeps debugging from turning into accidental redesign.

---

### 🔑 Principle 4: Debug in Two Phases

Just like planning/execution:

* **Phase A: Diagnosis (no code)**
* **Phase B: Fix (minimal diff)**

Never combine them unless the bug is trivial.

---

## 2️⃣ Example 1 — Data Science Debugging Prompt

### Scenario

A pandas-based pipeline is producing incorrect row counts after a cleaning step.

### ✅ Debugging Prompt (Diagnosis Mode)

```text
You are acting as a junior data scientist debugging a data pipeline.

Context:
- This code previously worked
- A recent change caused incorrect row counts after cleaning
- The pipeline uses pandas and pure functions

Task:
DEBUGGING ONLY — do not refactor or redesign.

Instructions:
1) Read the provided code and error/output description
2) Identify the most likely root cause(s)
3) Point to the exact line(s) of code responsible
4) Explain why the behavior occurs
5) Propose the minimal change required to fix it

Constraints:
- Do not change function signatures
- Do not introduce new dependencies
- Do not add new features
- Do not optimize performance

Do NOT write code yet.
Stop after diagnosis and wait for approval.
```

### Why this works

* Forces causal reasoning
* Anchors the AI to *existing behavior*
* Prevents “cleanup while debugging”
* Produces a reviewable explanation

---

### ✅ Follow-up Execution Prompt (After Approval)

```text
Using the approved diagnosis:

Apply the minimal fix described.

Constraints:
- Modify only the identified lines
- Preserve all existing behavior outside the bug
- Do not refactor or rename anything

Deliverable:
Code diff only.
```

---

## 3️⃣ Example 2 — Architecture / System-Level Debugging Prompt

### Scenario

A pipeline runs fine locally but fails when integrated into an application or job runner.

### ✅ Architecture Debugging Prompt (Diagnosis Mode)

```text
You are acting as a junior software engineer debugging a data pipeline integration issue.

Context:
- The pipeline logic is correct and tested
- Failures occur only when invoked via the application entry point
- No recent functional changes were made to the pipeline itself

Task:
DEBUGGING ONLY — diagnosis, not redesign.

Instructions:
1) Identify where assumptions between components may be mismatched
2) Trace the flow of inputs, configuration, and outputs across boundaries
3) Identify the most likely failure point(s)
4) Explain why the failure appears only in this execution context

Constraints:
- Do not propose architectural changes
- Do not introduce new frameworks
- Do not modify pipeline logic
- Focus only on configuration, invocation, or interface mismatches

Do NOT write code.
Stop after diagnosis and wait for approval.
```

### Why this works

* Focuses on **interfaces**, not internals
* Prevents AI from “fixing” the wrong layer
* Encourages boundary analysis (a common DS pain point)

---

### ✅ Follow-up Execution Prompt

```text
Using the approved diagnosis:

Apply the minimal fix needed to resolve the integration issue.

Constraints:
- Modify only the invocation/configuration layer
- Do not change pipeline behavior
- Preserve existing interfaces

Deliverable:
Code diff only.
```

---

## 4️⃣ Common Debugging Anti-Patterns (Avoid These)

### 🚫 “Fix this bug and clean up the code”

Invites scope creep + refactor drift.

### 🚫 “Improve error handling while fixing”

Error handling changes behavior — that’s not debugging anymore.

### 🚫 “Make it more robust”

Ambiguous and architectural.

### 🚫 Not providing expected vs actual behavior

AI needs *contrast* to reason correctly.

---

## 5️⃣ Signals That AI Is Going Off Track While Debugging

Watch for:

* suggestions to rename or reorganize files
* adding abstractions
* performance “improvements”
* changes not directly tied to the bug
* lack of causal explanation (“this should fix it”)

When you see that, stop and reset to **diagnosis-only mode**.

---

## The One Debugging Rule to Keep

> **If AI can’t explain *why* a bug occurs, it shouldn’t be allowed to fix it.**

This single rule will prevent ~80% of AI-assisted debugging failures.

---