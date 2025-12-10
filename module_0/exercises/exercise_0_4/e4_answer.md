**Python Code**
```python
from pydantic import BaseModel

class ExperimentResult(BaseModel):
    dataset_name: str
    samples_processed: int
    accuracy: float
    metadata: dict[str, str] | None = None

result = ExperimentResult(
    dataset_name=123,
    samples_processed="500",
    accuracy="high",
    metadata="not a dict"
)
```

**Validation Error Message**
```python
Traceback (most recent call last):
  File "C:\Projects\cs_foundations_for_agentic_multimodal_ai\module_0\exercises\exercise_4\e4_answer.py", line 9, in <module>
    result = ExperimentResult(
        dataset_name=123,
    ...<2 lines>...
        metadata="not a dict"
    )
  File "C:\Projects\cs_foundations_for_agentic_multimodal_ai\.venv\Lib\site-packages\pydantic\main.py", line 250, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 3 validation errors for ExperimentResult
dataset_name
  Input should be a valid string [type=string_type, input_value=123, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
accuracy
  Input should be a valid number, unable to parse string as a number [type=float_parsing, input_value='high', input_type=str]
    For further information visit https://errors.pydantic.dev/2.12/v/float_parsing
metadata
  Input should be a valid dictionary [type=dict_type, input_value='not a dict', input_type=str]
    For further information visit https://errors.pydantic.dev/2.12/v/dict_type
```