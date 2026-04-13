from agents.phase_agent import phase_agent
from agents.audit_agent import audit_agent
from agents.pentest_agent import pentest_agent
from agents.fix_agent import fix_agent

def run_hackgpt(query):
    state = {"query": query}
    state = phase_agent(state)
    state = audit_agent(state)
    state = pentest_agent(state)
    state = fix_agent(state)
    return state
