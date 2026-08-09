from typing import Literal
from pydantic import BaseModel, Field

Urgency = Literal["Low", "Medium", "High", "Critical"]

class AnalyzeRequest(BaseModel):
    complaint: str = Field(min_length=10, max_length=2000)

class AnalysisResult(BaseModel):
    category: str
    urgency: Urgency
    summary: str
    recommended_action: str
    department: str
    tags: list[str]
    ai_generated: bool
