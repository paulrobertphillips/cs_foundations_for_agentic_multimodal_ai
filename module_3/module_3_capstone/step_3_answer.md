Risk 1:
Description: assumption there's a fixed amount of bank account types that exist in finance dataset.
Where it first appears (Sprint X): Sprint 1.
Why it could accumulate: If database introduces new type of account, this may not be registered as a new "one hot encoded feature".
Mitigation: Write unit tests that ensure the number of new one hot encoded features equals the number of unique values in original feature.

Risk 2:
Description: input parameter name changes in feature engineering function definition to improve readability.
Where it first appears (Sprint X): Sprint 2.
Why it could accumulate: If logic containing feature engineering function call within pipeline is not updated to reflect refactoring changes made the pipeline would break when ran.
Mitigation: Run stabilization sprint to check for invariants & appropriate unit test coverage.
