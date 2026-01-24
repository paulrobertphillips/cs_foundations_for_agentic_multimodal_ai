# 🧭 **Guide: Translating the AI Review Checklist into Stakeholder Updates**

> **Purpose**
> Convert rigorous internal review into **clear, confidence-preserving stakeholder communication** — without over-disclosure or AI theater.

This guide assumes:

* the **One-Page AI Review Report Checklist** has been completed
* all conclusions are backed by evidence
* accountability is already clear internally

---

## The Core Translation Rule

> **Stakeholders care about outcomes, scope, and risk — not process mechanics.**

Your job is to **translate evidence into reassurance**, not explain how the evidence was produced.

---

## Step 1: Identify the Audience Tier

Before writing anything, answer one question:

> **Who is this update for?**

| Audience    | Primary Concern             |
| ----------- | --------------------------- |
| Executives  | Stability, risk, delivery   |
| Product     | Scope, readiness, tradeoffs |
| Engineering | Correctness, safeguards     |
| Compliance  | Traceability, control       |

This determines *how much* of the checklist you surface — not whether you surface it.

---

## Step 2: Map Checklist Sections to Message Themes

Here’s the key mapping. You don’t show the checklist — you **translate it**.

| Review Checklist Section | Stakeholder Message Theme         |
| ------------------------ | --------------------------------- |
| Scope adherence          | “Changes were limited to…”        |
| Behavior preservation    | “No functional behavior changed…” |
| Validation evidence      | “Validated via testing / review…” |
| Risk assessment          | “Risk is low / localized…”        |
| Ownership                | “Reviewed and approved by…”       |

If a checklist item doesn’t map cleanly, it probably doesn’t belong in the update.

---

## Step 3: Use the “What / What Not / How We Know” Pattern

Every good update can be structured as:

1. **What changed**
2. **What did not change**
3. **How we know**

This is the simplest way to:

* reduce anxiety
* demonstrate control
* preserve accountability

### Example skeleton

> This sprint focused on **[what changed]**.
> Importantly, **[what did not change]**.
> This was validated through **[how we know]**.

You’ll notice this pattern already appears in your past updates — that’s not an accident.

---

## Step 4: Translate AI Involvement Safely (When Needed)

If AI must be mentioned (engineering or compliance audiences):

* Use **tool framing**
* Emphasize **review**
* Avoid agency language

### Safe phrasing

* “AI was used as a productivity tool…”
* “AI-assisted refactoring was reviewed and approved…”
* “AI-generated suggestions were evaluated by engineers…”

### Avoid

* “AI decided…”
* “The model handled…”
* “We let AI refactor…”

---

## Step 5: Calibrate Detail — Don’t Equalize It

More detail ≠ more trust.

| Audience    | Detail Level           |
| ----------- | ---------------------- |
| Executives  | Minimal, outcome-based |
| Product     | Moderate, scope-aware  |
| Engineering | High, safeguard-aware  |
| Compliance  | Explicit, documented   |

**Never send the same update to all audiences.**

If you do, you’ll either:

* overshare and alarm executives, or
* undershare and frustrate engineers

---

## Step 6: Example Translations (Side-by-Side)

### Internal Review Checklist Conclusion (Source)

* Scope adhered to
* No behavior changes
* All tests passed
* Low risk
* Human-reviewed

---

### Executive Update (Derived)

> This sprint improved maintainability of the data ingestion step to support future scaling.
> No functional behavior changed, and the update was validated through existing tests.
> Risk is low and changes were reviewed prior to merge.

---

### Engineering Update (Derived)

> This sprint involved AI-assisted refactoring of the data ingestion module focused on readability and duplication reduction.
> Scope was limited to non-behavioral changes; all existing tests passed unchanged.
> AI-generated suggestions were reviewed and approved by engineers before merge.

Notice:

* Same facts
* Different emphasis
* Different level of detail

---

## Step 7: The Final Sanity Check

Before sending an update, ask:

> **“Could this message be misread as AI making decisions?”**

If yes → rewrite.

> **“Does this explain why risk is low without claiming perfection?”**

If no → add validation context.

---

## The Golden Rule (Worth Memorizing)

> **If the review checklist is strong, stakeholder communication becomes easy.
> If stakeholder communication feels hard, the review probably isn’t finished.**

That’s the loop working correctly.

---

## Where This Fits in the System (Final View)

* **AI Sprint Scope Contract** → constrain work
* **Decision Log** → preserve intent
* **Review Checklist** → validate outcomes
* **Stakeholder Update** → build trust

Nothing extra. Nothing wasted.

---