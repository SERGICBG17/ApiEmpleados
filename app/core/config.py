from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Config(BaseSettings):
    # Si no hay variable de entorno, el valor por defecto es None
    database_url: Optional[str] = None
    debug: bool = True

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

config = Config()