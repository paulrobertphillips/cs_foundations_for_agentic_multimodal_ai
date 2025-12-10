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