from langgraph.graph import Graph
from agents import receptionist_agent, sales_agent, support_agent, billing_agent

# Define the graph
workflow = Graph()

# Add nodes (agents)
workflow.add_node("receptionist", receptionist_agent)
workflow.add_node("sales", sales_agent)
workflow.add_node("support", support_agent)
workflow.add_node("billing", billing_agent)
workflow.add_node("end", lambda x: x)

# Define edges (routing logic)
def route_query(state):
    return state["department"]
    
workflow.add_conditional_edges(
    "receptionist",
    route_query,
    {
        "sales": "sales",
        "support": "support",
        "billing": "billing",
        "end": "end"
    }
)

# Add edges for agent responses
workflow.add_edge("sales", "end")
workflow.add_edge("support", "end")
workflow.add_edge("billing", "end")

# Set the entry point
workflow.set_entry_point("receptionist")

# Set the finish point
workflow.set_finish_point("end")

# Compile the graph
app = workflow.compile()