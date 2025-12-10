from pydantic import BaseModel
from typing import Optional

class SummaryResult(BaseModel):
    mean: float
    std: float

class AnalysisResult(BaseModel):
    row_count: Optional[int] = None
    column_count: Optional[int] = None
    summary: Optional[SummaryResult] = None
