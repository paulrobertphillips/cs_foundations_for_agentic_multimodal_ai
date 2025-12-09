# 🚀 Module 0.4 — Type Hints + Pydantic Models
<br>
Here’s your exercise if you'd like to try it:
<br>
<br>

**Create a Pydantic model named `ExperimentResult` with these fields:**
- `dataset_name`: str
- `samples_processed`: int
- `accuracy`: float
- `metadata`: dict[str, str] | None = None
Then try instantiating it with intentionally wrong types:

```
result = ExperimentResult(
    dataset_name=123,
    samples_processed="500",
    accuracy="high",
    metadata="not a dict"
)
```

Observe the `ValidationError`, and send me the code + result if you want feedback.

### 🔥 Why this matters specifically for agentic & multimodal AI

Agent frameworks (OpenAI function calling, LangChain, CrewAI, Autogen, etc.) rely on structured data schemas to:
- Validate tool inputs
- Validate tool outputs
- Prevent LLM hallucination
- Interpret user requests into typed objects
- Ensure the agent’s memory and state are type-safe
- Convert between Python objects ↔ JSON

Pydantic is the backbone of this in modern AI systems.

Think of Pydantic models as:

**“Guaranteed-correct containers for data passing between tools, agents, and models.”**

Type hints alone cannot do this.


### 🧠 Example showing the difference clearly


Without Pydantic (type hints only)

```
from typing import List

def process(values: List[int]) -> int:
    return sum(values)

process(["a", "b", "c"])  # Python LETS THIS HAPPEN

```
Result?
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'

```
### ➡️ The error happens deep inside the code, not at the boundary where you passed incorrect data.
<br>
That’s bad for agents, where inputs may come from an LLM.
---

With Pydantic

```
from pydantic import BaseModel
from typing import List

class Input(BaseModel):
    values: List[int]

inp = Input(values=["a", "b", "c"])

```
Result:
```
ValidationError: value is not a valid integer

```
➡️ Error happens immediately, at the boundary.
➡️ Much easier for agents to recover or correct themselves.
➡️ Much safer for pipelines.
