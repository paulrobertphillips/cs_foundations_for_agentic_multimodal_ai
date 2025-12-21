# 🧠 **Module 2 Capstone — Controlled AI-Assisted Refactor + Review**

## Capstone Goal

Demonstrate that you can:

1. **Use AI to refactor safely**
2. **Review AI-assisted changes rigorously**
3. **Produce auditable artifacts that build stakeholder trust**

This capstone mirrors how AI is used on strong engineering teams.

---

## 🧩 Capstone Scenario

You have a **working data ingestion + schema validation step**:

* Implemented with pandas
* Covered by tests
* Previously approved by stakeholders

You will:

* perform a **safe refactor** using AI
* conduct a **structured AI review**
* produce a **formal AI Review Report**

---

## 🧪 Capstone Structure (3 Phases)

---

## **Phase 1 — Safe Refactor (You already know how to do this)**

You’ve essentially practiced this in Module 2.4, so this phase should feel familiar.

### Step 1A — Refactor Planning Prompt (No Code)

Use your **Module 2.4 refactor planning prompt** pattern:

* explain intent
* lock scope
* list constraints
* require explanation before action

👉 You don’t need to resubmit this unless you want feedback — treat it as setup.

---

### Step 1B — Refactor Execution Prompt

Apply the approved plan:

* minimal diff
* no behavior change
* no architecture changes

Result: **refactored code + passing tests**

---

## **Phase 2 — AI Review Report (This is the new part)**

This is where we embed the **one-page checklist** into practice.

---

## 📄 AI Review Report — Templated Prompt (Auto-Filled)

You will use **this exact prompt** (copy/paste friendly).

You can fill in the bracketed sections as needed.

---

### ✅ **AI Review Report Prompt**

```text
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
  - <list filenames>
- Tests:
  - <list test files>
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

---

## **Phase 3 — Human-Facing Summaries**

From the AI Review Report, you now derive two artifacts:

### A) Review Checklist Summary

(3–5 bullets, internal)

### B) Stakeholder Update

(3–5 sentences, external)

You already practiced this in **Module 2.5** — this just makes it repeatable.

---

## 🧾 What You Should Produce for the Capstone

You don’t need to submit everything unless you want full review, but **at minimum**, aim to have:

1. ✅ Refactored code (safe, tested)
2. 📄 AI Review Report (Markdown)
3. 🧪 Review Checklist Summary
4. 📣 Stakeholder Update

Together, these form a **complete AI-assisted sprint artifact**.

---

## 🧠 Why This Capstone Matters

After this, you can confidently say:

* “I know how to control AI during development”
* “I know how to refactor safely with AI”
* “I know how to review and validate AI-assisted work”
* “I can produce artifacts stakeholders trust”

That’s not prompt tinkering — that’s **process ownership**.

---

## When You’re Ready

We can proceed in one of three ways:

1. **Step-by-step interactive** (like earlier modules)
2. **You draft the artifacts**, then I review them
3. **Hybrid**: you generate the AI Review Report first, we refine it together

Just tell me how you want to run the **Module 2 Capstone**, and we’ll start immediately.
