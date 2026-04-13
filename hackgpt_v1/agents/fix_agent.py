def fix_agent(state):
    fixes = []

    for issue in state.get("issues", []):
        if "SQL" in issue:
            fixes.append("Use parameterized queries")
        if "password" in issue.lower():
            fixes.append("Hash passwords with bcrypt")

    state["fixes"] = fixes or ["No fixes needed"]
    return state
