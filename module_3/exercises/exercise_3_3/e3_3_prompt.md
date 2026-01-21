# 🧪 **Module 3.3 — Mini-Exercise: Risk Accumulation Across Sprints**

## **Context (given)**

You’re reviewing a project that has completed **three AI-assisted sprints**:

* **Sprint 1:** Added missing-value handling for column `price`
* **Sprint 2:** Refactored feature engineering for reuse
* **Sprint 3:** Made model training reproducible (fixed seeds + splits)

Important facts:

* All tests pass
* No production incidents
* Each sprint, viewed alone, was AI-safe

Your task is to reason about **what can go wrong only when these are combined**.

---

## **Your Task**

Identify **two plausible accumulated risks** that could emerge *across* these sprints.

For **each risk**, explain:

1. **How it could arise** (the chain of reasoning)
2. **One concrete mitigation action** (lightweight, realistic)

---

## **Submission Format (use exactly this)**

```
Risk 1:
Description:
Mitigation:

Risk 2:
Description:
Mitigation:
```

---

## **What I’ll Be Looking For**

I’ll evaluate whether:

* the risks span **multiple sprints**
* the failure modes are **realistic**, not hypothetical
* mitigations are **proportional** (no over-engineering)
* your thinking reflects:

  * assumption drift
  * architectural entropy
  * validation gaps

There is **no single correct answer** — this exercise is about judgment and pattern recognition.

Take your time. When you’re ready, submit your two risks and mitigations, and we’ll review them together.
