**Python Code**
```python
from pydantic import BaseModel

# Note: BaseModel seems to hand @dataclass already
class Trial(BaseModel):
    id: int
    score: float

class Experiment(BaseModel):
    name: str
    trials: list[Trial]

exp = Experiment(
    name="test_experiment",
    trials=[
        {"id": "not an int", "score": "NaN"},
        {"id": 2, "score": 0.9}
    ]
)
```

**Validation Error Message**
```python
Traceback (most recent call last):
  File "C:\Projects\cs_foundations_for_agentic_multimodal_ai\module_0\exercises\exercise_4\bonus_answer.py", line 12, in <module>
    exp = Experiment(
        name="test_experiment",
    ...<3 lines>...
        ]
    )
  File "C:\Projects\cs_foundations_for_agentic_multimodal_ai\.venv\Lib\site-packages\pydantic\main.py", line 250, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for Experiment
trials.0.id
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='not an int', input_type=str]
    For further information visit https://errors.pydantic.dev/2.12/v/int_parsing
```