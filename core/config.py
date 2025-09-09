from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class DBSettings(BaseModel):
    url:str = f"sqlite+aiosqlite:///{}"
    echo:bool = False