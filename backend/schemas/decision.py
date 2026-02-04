from pydantic import BaseModel, Field
from typing import List, Optional

class Option(BaseModel):
    name: str
    description: Optional[str] = None


class DecisionPlan(BaseModel):
    question: str
    options: List[Option] = Field(..., min_items=2)
    criteria: List[str] = Field(..., min_items=1)
