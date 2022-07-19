import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    app_host: str
    app_port: int
    flespi_token: str
    flespi_base_url: str
    flespi_messages_url: str


def load_from_env() -> AppConfig:
    return AppConfig(
        app_host=os.environ['APP_HOST'],
        app_port=int(os.environ['APP_PORT']),
        flespi_token=os.environ['FLESPI_TOKEN'],
        flespi_base_url=os.environ['FLESPI_BASE_URL'],
        flespi_messages_url=os.environ['FLESPI_MESSAGES'],
    )


app_config = load_from_env()
