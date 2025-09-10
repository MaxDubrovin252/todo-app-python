from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")


class DBSettings(BaseModel):
    url:str = DB_URL
    echo:bool = False
    
    
class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    
    
    
settings = Settings()