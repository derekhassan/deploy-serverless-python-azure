# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from re import compile, IGNORECASE

CODE_FORM_PATTERN = compile(r'^[a-z]{5}-\d{5}-[a-z]{5}$', IGNORECASE)


def main(code: str) -> str:
    if CODE_FORM_PATTERN.match(code):
        return code.lower()
    return ''
