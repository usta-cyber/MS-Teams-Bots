import os

class DefaultConfig:
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")


#python3.10 -m aiohttp.web -H 0.0.0.0 -P 8000 app:init_func
