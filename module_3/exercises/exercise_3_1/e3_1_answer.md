## Tasks to Classify

**1. Writing a CSV ingestion function with a fixed schema -** 🟢

Data ingestion task is bounded by a fixed schema, which means AI will understand the assumptions being made about the CSV file (authoritative/proxy/heuristic, data types, data use objectives, etc.). Mistakes at this stage of work are also considered highly reversible.

**2. Designing the overall system architecture for production -** 🔴

Overall system architecture design task is very abstract, which means it will not be well bounded. Even with a human-led attempt to bound system architecture design constraints it's likely AI will diverge or hallucinate due to the complexity of taking on architecture design & implementation as a single task. Mistakes are not reversible at this stage because it'd be as expensive for the human developer to learn the AI-created architecture as it would for them to start from scratch.

**3. Refactoring a working data pipeline to reduce duplication -** 🔴

Similar to using AI to design & implement a system architecture in one go, AI should not be used to refactor an entire data pipeline in one go. The system-level reasoning AI must forego would be complex and abstract, even if constraints & objectives within each step are clearly defined. The risk here is AI hallucinating in its reasoning for refactoring across the pipeline. Mistakes are also not considered reversible for similar reasons mentioned with using AI to do system architecture development.

**4. Choosing the target metric for a business decision -** 🟢

Choosing target metrics for a business decision would be clearly bounded by objectives of the business decision being supported. Mistakes would also considered reversible, since this task would be a part of protyping some new solution.

**5. Debugging a failing unit test with a known error message -** 🟢

Debugging a failing unit test would be clearly bound since AI would be focused on cause and effect of the received error message. Depending on the size/magnitude of the bug, mistake reversibility can be considered feasible (example: fixing a bug found in a function).

**6. Deciding when to retrain a model in production -** 🔴

Deciding when to retrain a model in production would be clearly bounded, but this infers AI would own the mainenance portion of a solution that's been moved into production. Mistakes should be viewed irreversible in this regard. That, and AI should not be made owner of any portion of a solution whether in the development stage or production.

**7. Generating a stakeholder sprint update -** 🟢

Generating a stakeholder sprint update would be bounded since AI would just be summarizing the work that has been scoped & executed within a given sprint. Mistakes of summaries are also considered reversible since humans can easily digest the outcome and correct as needed.