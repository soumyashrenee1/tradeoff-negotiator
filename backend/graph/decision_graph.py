from langgraph.graph import StateGraph
from graph.state import DecisionState

from agents.planner import planner_node
from agents.cost_agent import cost_node
from agents.speed_agent import speed_node
from agents.quality_agent import quality_node
from agents.risk_agent import risk_node
from agents.mediator import mediator_node


def build_graph():
    graph = StateGraph(DecisionState)

    graph.add_node("planner", planner_node)
    graph.add_node("cost", cost_node)
    graph.add_node("speed", speed_node)
    graph.add_node("quality", quality_node)
    graph.add_node("risk", risk_node)
    graph.add_node("mediator", mediator_node)

    graph.set_entry_point("planner")

    # fan-out
    graph.add_edge("planner", "cost")
    graph.add_edge("planner", "speed")
    graph.add_edge("planner", "quality")
    graph.add_edge("planner", "risk")

    # fan-in
    graph.add_edge("cost", "mediator")
    graph.add_edge("speed", "mediator")
    graph.add_edge("quality", "mediator")
    graph.add_edge("risk", "mediator")

    graph.set_finish_point("mediator")

    return graph.compile()
