from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "todo.db"


class DBSettings(BaseModel):
    url:str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo:bool = False
    
    
class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    
    
    
settings = Settings()