from typing import TypedDict, Annotated, Sequence
import operator
from langgraph.graph import StateGraph, END
from agents.nodes.navigation import navigate_and_capture
from agents.nodes.vision_analysis import analyze_ui_heuristics

class AuditorState(TypedDict):
    url: str
    goal: str
    current_step: int
    screenshots: Annotated[Sequence[str], operator.add]
    issues_found: Annotated[Sequence[dict], operator.add]
    is_complete: bool

def route_next_step(state: AuditorState):
    if state["is_complete"] or state["current_step"] > 5:
        return END
    return "navigate"

workflow = StateGraph(AuditorState)

# Define the nodes
workflow.add_node("navigate", navigate_and_capture)
workflow.add_node("analyze", analyze_ui_heuristics)

# Build the edges
workflow.set_entry_point("navigate")
workflow.add_edge("navigate", "analyze")
workflow.add_conditional_edges("analyze", route_next_step)

# Compile the autonomous agent
auditor_agent = workflow.compile()
