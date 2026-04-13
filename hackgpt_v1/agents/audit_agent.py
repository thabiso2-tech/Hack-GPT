def audit_agent(state):
    query = state["query"].lower()
    issues = []

    if "sql" in query:
        issues.append("Possible SQL Injection vulnerability")

    if "password" in query:
        issues.append("Weak password handling")

    state["issues"] = issues or ["No obvious issues detected"]
    return state
