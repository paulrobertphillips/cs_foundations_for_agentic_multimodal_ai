# 🧪 **Module 3.2 — Mini-Exercise**

You’ll take **vague, AI-dangerous sprint tickets** and rewrite them into **AI-safe, vertically sliced sprint tickets**.

Remember what we just clarified:

* Horizontal = *areas / pipeline stages* ❌
* Vertical = *specific, end-to-end behaviors* ✅
* Safety is about **boundedness, reviewability, and blast radius**, not sprint size.

---

## 🚨 Original Sprint Tickets (Problematic)

1. **“Clean the dataset so it’s ready for modeling.”**
2. **“Improve the data pipeline and make it more maintainable.”**
3. **“Prepare the model training step for production use.”**

---

## 🎯 Your Task

For **each ticket**, rewrite it as an **AI-safe sprint ticket** with:

* **Sprint goal** (1–2 sentences, outcome-focused)
* **In scope** (explicit permissions)
* **Out of scope** (explicit exclusions)
* **Acceptance criteria** (objective, testable)

Each rewritten ticket should:

* represent a **vertical slice**
* have a **clear stop condition**
* be reviewable without re-learning the system
* have a **low blast radius**

---

## 📝 Submission Format (use exactly this)

```
### Ticket 1

Sprint goal:
...

In scope:
- ...

Out of scope:
- ...

Acceptance criteria:
- ...

### Ticket 2
...

### Ticket 3
...
```

---

## What I’ll Review For

I’ll check that:

* horizontal work has been decomposed into vertical slices
* acceptance criteria are concrete and verifiable
* architectural drift is explicitly excluded
* the tickets are genuinely AI-executable

Once we finish this, we’ll move straight into
**Module 3.3 — Managing Risk Accumulation Across Sprints**.

Take your time — this exercise is one of the most important practical skills in AI-driven project leadership.

# Appendix

## What “Prepare Model Training for Production” *Usually* Means

In real projects, this phrase is often shorthand for a *bundle* of smaller tasks.

Here are the most common categories it actually includes:

---

### 1️⃣ Determinism & Reproducibility (Very Common)

Making sure that:

* the same data + config → same model
* randomness is controlled
* runs can be reproduced later

Concrete examples:

* setting random seeds
* fixing train/validation splits
* logging hyperparameters
* logging dataset version identifiers

⚠️ This is **AI-safe when scoped narrowly**.

---

### 2️⃣ Inputs & Interfaces (Very Common)

Making sure:

* training expects a well-defined input format
* features are named and typed explicitly
* schema mismatches fail loudly

Concrete examples:

* validating feature columns before training
* checking target column presence
* asserting data types

⚠️ This is **AI-safe when scoped**.

---

### 3️⃣ Configuration Externalization (Common)

Moving “magic values” out of code:

* learning rate
* number of epochs
* regularization strength

Concrete examples:

* config file or dict
* environment-based overrides

⚠️ Safe **if limited to wiring, not redesign**.

---

### 4️⃣ Observability & Reporting (Common)

Making training *inspectable*:

* logging metrics
* saving artifacts
* reporting run summaries

Concrete examples:

* log training loss
* save model with version tag
* output a simple run report

⚠️ Safe **if no deployment logic is added**.

---

### 5️⃣ What It Does *NOT* Mean (Often Misunderstood)

“Prepare for production” does **not automatically mean**:

* deploy the model
* build CI/CD
* set up monitoring
* autoscaling
* retraining policies
* inference services

Those are **separate phases** and much riskier.

---

## Why the Original Ticket Is AI-Dangerous

Because it implicitly bundles **all five categories** above, without saying which ones apply.

AI will:

* guess what “production” means
* over-engineer
* introduce architecture
* cross ownership boundaries

That’s why the ticket must be decomposed.

---

## How You Should Think About Rewriting Ticket 3

Instead of asking:

> “How do I prepare model training for production?”

Ask:

> **“Which *one* production-readiness property am I making true in this sprint?”**

Examples of **AI-safe vertical slices** you could choose:

* Make training deterministic
* Validate training input schema
* Externalize training hyperparameters
* Produce a training run report

Each of these is:

* bounded
* reviewable
* reversible
* testable

---

## A Concrete Example (Just One Option)

Here’s **one** possible vertical slice you could use for Ticket 3:

> **Sprint goal:**
> Make the model training step reproducible by enforcing deterministic behavior and logging training configuration.

This avoids:

* deployment
* architecture
* ownership decisions

And focuses on **behavior**, not systems.

---
