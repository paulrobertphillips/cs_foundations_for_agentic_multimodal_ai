
## Module 3 Capstone — Step-by-Step Plan

### Step 4 — Governance & Escalation Points

Now we answer:

> “How do we know when this plan is no longer safe, and what do we do then?”

### Your output for Step 4 should cover:

* What changes require **extra review**
* What signals trigger a **stabilization sprint**
* When AI usage should be **paused or further constrained**

Use this format:

```
Extra Review Required When:
- …

Stabilization Sprint Triggered When:
- …

AI Usage Escalation / Constraint When:
- …
```

Think in terms of **signals**, not policies:

* test failures
* unexpected data behavior
* growing uncertainty
* stakeholder discomfort

Whenever you’re ready, submit **Step 4**.

# Appendix

## What Step 4 *Is Not*

You are **not**:

* writing company-wide policies
* defining permanent rules
* pre-scheduling sprints
* creating process overhead

You are **not saying**:

> “Whenever X happens, the team must do Y.”

---

## What Step 4 *Actually Is*

Step 4 is about defining **early warning signals** and **response levers**.

Think of it as answering three questions:

1. **When should we slow down?**
2. **When should we pause and stabilize instead of building?**
3. **When should we reduce or restrict AI involvement because risk has increased?**

This is *situational judgment*, not bureaucracy.

---

## Reframing the Three Sections

### 1️⃣ **“Extra Review Required When”**

This answers:

> *When is normal peer review no longer enough?*

These are **signals that the work has become more consequential** than originally planned.

Examples of what this really means:

* “This change affects downstream consumers”
* “Assumptions are less clear than expected”
* “We touched code that wasn’t originally in scope”

You’re saying:

> *If we see these signals, we add more human eyes.*

Not a rule — a **pause-and-check instinct**.

---

### 2️⃣ **“Stabilization Sprint Triggered When”**

This answers:

> *When should we stop adding features and focus on restoring confidence?*

A stabilization sprint is **reactive**, not planned in advance.

This section defines the *conditions* that justify one.

Think of it as:

* uncertainty is increasing
* behavior is changing faster than understanding
* tests exist but confidence is dropping

You’re saying:

> *If these signals show up, the next sprint should reduce risk, not add capability.*

---

### 3️⃣ **“AI Usage Escalation / Constraint When”** (the confusing one)

This does **not** mean “escalate AI usage”.

It means:

> *Escalate the level of caution applied to AI.*

In other words:

* narrow what AI is allowed to do
* shift AI from execution → analysis → planning
* temporarily forbid AI from certain tasks

This answers:

> *When does AI become less safe than it was before?*

You are defining **conditions under which AI’s role should shrink**, not grow.

That’s why “constraint” is the important word here.

---

## A Concrete Example Using *Your* Project

Let’s map this to your capstone context.

### You are working on:

* feature engineering
* refactoring
* stabilization

### Over time, you might notice:

* assumptions about account types are shakier
* more exceptions are being handled ad hoc
* refactors touch more pipeline steps than expected

Step 4 is where you say:

> *“If we start seeing these patterns, we deliberately slow down and tighten control.”*

---

## How to Think About This Mentally

A good way to internalize Step 4:

> **Step 1–3 define what we plan to do.
> Step 4 defines how we notice when that plan is no longer safe.**

It’s a *feedback system*, not a rulebook.

---

## Now: How You Should Answer Step 4

When you write Step 4, don’t think:

> “What rules should exist?”

Instead think:

> “What would make me uncomfortable if I saw it happening mid-project?”

Then turn that discomfort into:

* a signal
* a response

---

## Ready for a Simpler Restatement of the Task?

For Step 4, you are defining:

* **Signals that increase risk**
* **The appropriate response to those signals**

Nothing more.

---
