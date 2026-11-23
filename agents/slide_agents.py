
def question_agent(question, context):

    if not context:
        return "I could not find relevant information in the presentation."

    answer_parts = []

    for block in context:
        answer_parts.append(
            f"{block['block_id']}: {block['content']}"
        )

    answer = " ".join(answer_parts)

    return (
        f"Based on the presentation, here is the information "
        f"relevant to your question: {answer}"
    )


def comparison_agent(question, context):

    if len(context) < 2:
        return "I need information from at least two slides to make a comparison."

    comparison_parts = []

    for block in context:
        comparison_parts.append(
            f"{block['block_id']} explains: {block['content']}"
        )

    comparison = "\n".join(comparison_parts)

    return (
        f"Here is the comparison based on the available slides:\n"
        f"{comparison}"
    )


def summary_agent(question, context):

    if not context:
        return "There is no relevant slide information to summarize."

    summary_parts = []

    for block in context:
        summary_parts.append(block["content"])

    summary = " ".join(summary_parts)

    return (
        f"Here is a summary of the relevant presentation information: "
        f"{summary}"
    )


def select_slide_agent(question):

    normalized_question = question.lower()

    comparison_keywords = [
        "compare",
        "comparison",
        "difference",
        "differences",
        "versus",
        "vs"
    ]

    summary_keywords = [
        "summarize",
        "summary",
        "overview",
        "briefly explain"
    ]

    if any(keyword in normalized_question for keyword in comparison_keywords):
        return comparison_agent

    if any(keyword in normalized_question for keyword in summary_keywords):
        return summary_agent

    return question_agent


def run_slide_agent(question, context):

    selected_agent = select_slide_agent(question)

    print(f"\n[AGENT] Selected agent: {selected_agent.__name__}")

    answer = selected_agent(question, context)

    return {
        "agent_name": selected_agent.__name__,
        "answer": answer
    }
