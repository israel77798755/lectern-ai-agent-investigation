
def finalizer_node(state):

    print("\n[FINALIZER NODE] Finalizing workflow...")

    answer = state.get("answer", "")
    citation_valid = state.get("citation_valid", False)
    answer_attempts = state.get("answer_attempts", 0)
    step_count = state.get("step_count", 0)
    step_cap = state.get("step_cap", 10)

    if step_count >= step_cap:

        outcome = "step_cap_reached"

    elif not answer:

        outcome = "failed"

    elif not citation_valid:

        outcome = "invalid_citations"

    else:

        outcome = "success"

    state["outcome"] = outcome
    state["final_answer"] = answer
    state["completed"] = True

    print(f"[FINALIZER NODE] Answer attempts: {answer_attempts}")
    print(f"[FINALIZER NODE] Steps executed: {step_count}")
    print(f"[FINALIZER NODE] Final outcome: {outcome}")

    return state
