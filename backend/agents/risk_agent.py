from graph.state import DecisionState
from schemas.agent_score import AgentScore
from langchain_openai import ChatOpenAI
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def risk_node(state: DecisionState) -> dict:
    plan = state.plan

    prompt = f"""
You are a RISK-focused decision analyst.

Evaluate each option ONLY on:
- likelihood of failure
- security or compliance risk
- long-term uncertainty

Options:
{[opt.name for opt in plan.options]}

Return STRICT JSON:
{{
  "scores": {{
    "option_name": number_between_0_and_10
  }},
  "reasoning": "short explanation"
}}
"""

    response = llm.invoke(prompt)
    parsed = json.loads(response.content)

    return {
        "agent_outputs": [
            AgentScore(
                agent="risk",
                scores=parsed["scores"],
                reasoning=parsed["reasoning"]
            )
        ]
    }
