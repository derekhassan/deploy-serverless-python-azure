# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    data = context._input
    code = json.loads(data)

    result1 = yield context.call_activity('CheckCodeForm', code)

    logging.info(f"Result1 is: {result1}")

    result2 = yield context.call_activity('CheckCodeUsed', code)
    result3 = yield context.call_activity('GenerateLink', code)
    return [result1, result2, result3]


main = df.Orchestrator.create(orchestrator_function)
