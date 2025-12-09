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