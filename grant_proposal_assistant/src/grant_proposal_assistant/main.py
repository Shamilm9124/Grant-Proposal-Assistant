#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from grant_proposal_assistant.crew import GrantProposalAssistant
from grant_proposal_assistant.tools.custom_tool import WordLimitChecker
word_checker = WordLimitChecker()
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the Grant Proposal Assistant crew.
    """

    inputs = {
        "project_name": "Community Digital Literacy Program",

        "project_goal": (
            "Provide digital literacy training for underprivileged "
            "students in rural communities."
        ),

        "funding_request": "$25,000",

        "project_duration": "12 months",

        "target_beneficiaries": (
            "High school students from low-income rural areas."
        ),

        "grant_type": "Education Development Grant",

        "current_year": str(datetime.now().year)
    }

    result =GrantProposalAssistant().crew().kickoff(inputs=inputs)

    # Word limit validation
    word_limit_result = word_checker.check(
        text=str(result),
        limit=1500
    )
    print("\n===== WORD LIMIT CHECK =====")
    print(word_limit_result)



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        GrantProposalAssistant().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        GrantProposalAssistant().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        GrantProposalAssistant().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = GrantProposalAssistant().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
