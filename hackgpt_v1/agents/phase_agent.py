def phase_agent(state):
    state["plan"] = f"Analyze and secure: {state['query']}"
    return state
