
from nodes.context import context_node
from nodes.citation import citation_node
from nodes.finalizer import finalizer_node
from agents.slide_agents import run_slide_agent


def answer_template():

    return {
        "name": "answer_template",
        "nodes": [
            context_node,
            run_slide_agent,
            citation_node,
            finalizer_node
        ],
        "step_cap": 10
    }


def get_template(template_name):

    templates = {
        "answer_template": answer_template
    }

    template_factory = templates.get(template_name)

    if template_factory is None:
        raise ValueError(
            f"Template '{template_name}' does not exist."
        )

    return template_factory()
