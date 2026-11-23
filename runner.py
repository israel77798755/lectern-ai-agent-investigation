
import json
from pathlib import Path

from nodes.context import context_node
from nodes.answer import answer_node
from nodes.citation import citation_node
from nodes.finalizer import finalizer_node


PROJECT_DIR = Path(__file__).resolve().parent
SLIDES_FILE = PROJECT_DIR / "data" / "slides.json"


def load_slides():

    if not SLIDES_FILE.exists():
        raise FileNotFoundError(
            f"Slides file not found: {SLIDES_FILE}"
        )

    with open(SLIDES_FILE, "r", encoding="utf-8") as file:
        slides = json.load(file)

    if not isinstance(slides, dict):
        raise ValueError(
            "The slides file must contain a JSON object."
        )

    return slides


def execute_node(node, state):

    state["step_count"] += 1

    print("\n" + "=" * 50)
    print(f"Executing: {node.__name__}")
    print(f"Workflow step: {state['step_count']}")
    print("=" * 50)

    return node(state)


def run_answer_template(question, slides):

    state = {
        "question": question,
        "slides": slides,
        "context": [],
        "answer": "",
        "final_answer": "",
        "answer_attempts": 0,
        "citation_valid": False,
        "invalid_citations": [],
        "citation_message": "",
        "step_count": 0,
        "step_cap": 10,
        "outcome": None,
        "completed": False
    }

    workflow_nodes = [
        context_node,
        answer_node,
        citation_node,
        finalizer_node
    ]

    for node in workflow_nodes:

        if state["step_count"] >= state["step_cap"]:
            print("\n[RUNNER] Maximum step limit reached.")
            break

        state = execute_node(node, state)

    return state


def main():

    print("\nLECTERN AI AGENT INVESTIGATION")
    print("=" * 50)

    try:
        slides = load_slides()

        print(f"Loaded {len(slides)} slides successfully.")

        question = input("\nEnter your question: ").strip()

        if not question:
            print("Please enter a valid question.")
            return

        result = run_answer_template(question, slides)

        print("\n" + "=" * 50)
        print("WORKFLOW RESULTS")
        print("=" * 50)

        print(f"Question: {result['question']}")
        print(f"Answer: {result['final_answer']}")
        print(f"Citations valid: {result['citation_valid']}")
        print(f"Answer attempts: {result['answer_attempts']}")
        print(f"Steps executed: {result['step_count']}")
        print(f"Final outcome: {result['outcome']}")

    except (FileNotFoundError, ValueError, json.JSONDecodeError) as error:
        print(f"\n[ERROR] {error}")


if __name__ == "__main__":
    main()
