
import re


def citation_node(state):

    print("\n[CITATION NODE] Validating answer citations...")

    answer = state.get("answer", "")
    context = state.get("context", [])

    available_block_ids = {
        block["block_id"]
        for block in context
    }

    cited_block_ids = re.findall(
        r"slide_\d+",
        answer
    )

    invalid_citations = []

    for citation in cited_block_ids:

        if citation not in available_block_ids:
            invalid_citations.append(citation)

    if not cited_block_ids:

        state["citation_valid"] = False
        state["invalid_citations"] = []
        state["citation_message"] = "No citations were found."

    elif invalid_citations:

        state["citation_valid"] = False
        state["invalid_citations"] = invalid_citations
        state["citation_message"] = "Some citations do not exist in the context."

    else:

        state["citation_valid"] = True
        state["invalid_citations"] = []
        state["citation_message"] = "All citations are valid."

    print(f"[CITATION NODE] Found citations: {cited_block_ids}")
    print(f"[CITATION NODE] Invalid citations: {invalid_citations}")
    print(f"[CITATION NODE] Result: {state['citation_message']}")

    return state
