# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

from random import randint, seed


def main(code: str) -> str:
    seed(code)
    if 1 == randint(0, 1):
        return code.lower()
    return ''
