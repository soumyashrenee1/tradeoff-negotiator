from graph.state import DecisionState
from schemas.decision import DecisionPlan, Option
from langchain_openai import ChatOpenAI
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def planner_node(state: DecisionState) -> dict:
    # Case 1: options already exist
    if state.options:
        return {
            "plan": DecisionPlan(
                question=state.question,
                options=state.options,
                criteria=list(state.weights.keys())
            )
        }

    # Case 2: infer options + criteria
    prompt = f"""
You are a decision analyst.

Infer:
1. 2–5 OPTIONS
2. Evaluation CRITERIA

Return STRICT JSON:
{{
  "options": [{{"name": "...", "description": "..."}}],
  "criteria": ["...", "..."]
}}

Question:
{state.question}
"""

    response = llm.invoke(prompt)
    parsed = json.loads(response.content)

    options = [Option(**o) for o in parsed["options"]]

    return {
        "plan": DecisionPlan(
            question=state.question,
            options=options,
            criteria=parsed["criteria"]
        )
    }
