import os
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    model: str = os.getenv("MODEL", "gemini-2.5-flash")
    reorder_threshold: int = 10

config = Config()
