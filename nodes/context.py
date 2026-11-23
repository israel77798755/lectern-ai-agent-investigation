
def context_node(state):
    """
    Prepare the slide context before generating an answer.
    """

    print("\n[CONTEXT NODE] Preparing slide context...")

    question = state["question"]
    slides = state["slides"]

    # For this simulation, make all slides available as context.
    context = []

    for slide_number, slide_content in slides.items():
        context.append({
            "block_id": f"slide_{slide_number}",
            "content": slide_content
        })

    # Save the prepared context in the shared state.
    state["context"] = context

    print(f"[CONTEXT NODE] Prepared {len(context)} slide blocks.")

    return state
