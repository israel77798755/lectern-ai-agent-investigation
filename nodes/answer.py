
def answer_node(state):
    """
    Generate an answer using the question and prepared slide context.

    This node receives the shared state, reads the user's question,
    examines the available slide context, and generates an answer.
    """

    print("\n[ANSWER NODE] Generating an answer...")

    # Step 1: Read the question from the shared state.
    question = state["question"]

    # Step 2: Read the context prepared by the context node.
    context = state["context"]

    # Step 3: Initialize an empty list for relevant slide information.
    relevant_slides = []

    # Step 4: Search through the context for slides mentioned
    # in the question.
    for block in context:

        block_id = block["block_id"]
        content = block["content"]

        # Extract the slide number from the block ID.
        slide_number = block_id.replace("slide_", "")

        # Check whether the slide number appears in the question.
        if slide_number in question:
            relevant_slides.append({
                "block_id": block_id,
                "content": content
            })

    # Step 5: Generate an answer using the relevant slide information.
    if relevant_slides:

        answer_parts = []

        for slide in relevant_slides:

            answer_parts.append(
                f"{slide['block_id']}: {slide['content']}"
            )

        answer = (
            "Here is the relevant information from the slides: "
            + " | ".join(answer_parts)
        )

    else:

        answer = (
            "I could not find any relevant slide information "
            "to answer the question."
        )

    # Step 6: Store the generated answer in the shared state.
    state["answer"] = answer

    # Step 7: Record that the answer node has executed.
    state["answer_attempts"] = state.get("answer_attempts", 0) + 1

    print("[ANSWER NODE] Answer generated successfully.")
    print(f"[ANSWER NODE] Execution count: {state['answer_attempts']}")

    return state
