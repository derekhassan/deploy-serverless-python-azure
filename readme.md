source .venv/bin/activate

1. Make `local.settings.json`:

```json
{
    "isEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
        "FUNCTIONS_WORKER_RUNTIME": "python"
    }
}
```
