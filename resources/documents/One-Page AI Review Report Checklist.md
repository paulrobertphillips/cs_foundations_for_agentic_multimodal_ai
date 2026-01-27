# ✅ One-Page AI Review Report Checklist

Below is a **one-page AI Review Report Checklist** designed to be:

* quick to apply
* copy-paste friendly
* usable with *any* AI tool
* aligned with everything you learned in Module 2

You can think of this as the *minimum viable governance layer* for AI-assisted engineering.

**For AI-Assisted Code & Data Science Work**

---

## 1️⃣ Review Context (Required)

[] Review type clearly stated
    Examples: refactor, bug fix, feature addition, integration change

[] Scope explicitly defined
    What files / components were reviewed

[] Out-of-scope items explicitly listed
    What was *not* reviewed or intentionally excluded

[] AI role declared
    Example: “AI acting as constrained reviewer”

---

## 2️⃣ Inputs Reviewed (Evidence)

[] Code files listed
    Exact filenames or modules

[] Tests reviewed or executed
    Test names or test suite

[] Reference artifacts included
    Sprint plan, refactor plan, design notes (if applicable)

[] Inputs are complete
    No undocumented assumptions about missing context

---

## 3️⃣ Review Checks Performed

[] Scope adherence verified
    No work outside approved sprint/refactor plan

[] Behavior preservation confirmed (if applicable)
    Same inputs → same outputs

[] Public interfaces checked
    Function signatures, schemas, contracts unchanged

[] Dependency changes checked
    No new dependencies unless approved

[] Configuration / invocation unchanged (if relevant)

---

## 4️⃣ Test Evidence

[] Tests executed (Yes / No)

[] Test results recorded
    Passed: ___
    Failed: ___

[] New tests added?
    If yes, list them
    If no, explicitly state “None”

[] Known untested cases acknowledged

---

## 5️⃣ Behavior & Interface Verification

[] Input formats unchanged

[] Output formats unchanged

[] Data contracts preserved

[] Error behavior unchanged (unless explicitly scoped)

[] Downstream consumers unaffected

---

## 6️⃣ Findings Summary

[] Confirmed safe changes listed
    (What *did* change)

[] Issues identified (if any)
    Or explicitly state “None observed”

[] Claims backed by evidence
    No unsupported assertions

---

## 7️⃣ Risk Assessment

[] Overall risk level stated
    Low / Medium / High

[] Rationale provided
    Why this risk level is appropriate

[] Mitigations identified (if needed)

[] Remaining unknowns acknowledged

---

## 8️⃣ Review Limitations (Required)

[] Explicit statement of what this review does **not** guarantee

Examples:

* Performance under scale not evaluated
* Production environment behavior not tested
* Edge cases outside test coverage

[] No false sense of certainty conveyed

---

## 9️⃣ Final Sanity Check

[] Review output is factual, not speculative

[] No refactor or improvement suggestions slipped in

[] Language is conservative and review-appropriate

[] A human could defend this review to a stakeholder

---

## 🧠 Rule of Thumb (Put This at the Bottom)

> **If a claim cannot be traced to code, tests, or an explicit assumption, it does not belong in the review.**

---

### How to Use This in Practice

* Paste this checklist into:

  * a PR description
  * a review prompt
  * a sprint artifact
  * a governance doc
* You do *not* need to fill every item every time — but you should **explicitly skip** items that don’t apply.

---
