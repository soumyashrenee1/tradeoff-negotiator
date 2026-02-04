from typing import List, Dict, Annotated, Optional
from pydantic import BaseModel
import operator

from schemas.decision import DecisionPlan
from schemas.agent_score import AgentScore

class DecisionState(BaseModel):
    # Provided by API
    question: str
    options: list = []
    weights: Dict[str, float]

    # Created by planner
    plan: Optional[DecisionPlan] = None

    # Parallel-safe
    agent_outputs: Annotated[List[AgentScore], operator.add] = []

    # Final
    final_decision: dict | None = None
