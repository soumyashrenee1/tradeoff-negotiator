from graph.state import DecisionState
from collections import defaultdict

def mediator_node(state: DecisionState) -> dict:
    """
    Combines agent scores using user-defined weights.
    Produces the final decision.
    """

    weights = state.weights
    agent_outputs = state.agent_outputs

    # option -> weighted total
    totals = defaultdict(float)

    # option -> breakdown per agent
    breakdown = defaultdict(dict)

    for agent_score in agent_outputs:
        agent = agent_score.agent
        weight = weights.get(agent, 1.0)  # default weight = 1

        for option, score in agent_score.scores.items():
            weighted = score * weight
            totals[option] += weighted
            breakdown[option][agent] = {
                "raw_score": score,
                "weight": weight,
                "weighted_score": weighted,
                "reasoning": agent_score.reasoning
            }

    if not totals:
        return {
            "final_decision": {
                "error": "No agent scores available"
            }
        }

    best_option = max(totals, key=totals.get)

    return {
        "final_decision": {
            "best_option": best_option,
            "final_scores": dict(totals),
            "breakdown": dict(breakdown),
            "weights": weights
        }
    }
