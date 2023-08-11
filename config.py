import os

class DefaultConfig:
    PORT = 3978
    # APP_ID = os.environ.get("MicrosoftAppId", "")
    # APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_ID = os.environ.get("MicrosoftAppId", "49668c1f-c8f6-491a-ae9d-709143924630")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "137c2d23-a2f9-4424-ab7c-3bec4387875f")

#python3.10 -m aiohttp.web -H 0.0.0.0 -P 8000 app:init_func