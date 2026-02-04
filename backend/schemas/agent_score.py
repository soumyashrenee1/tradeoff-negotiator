from pydantic import BaseModel
from typing import Dict

class AgentScore(BaseModel):
    agent: str
    scores: Dict[str, float]  # option -> score (0–10)
    reasoning: str
