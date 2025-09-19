from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")

class JWTSettings(BaseModel):
    secret_key:str= os.getenv("SECRET_KEY")
    exp_time:int = os.getenv("ACCESS_TOKEN_EXP")


class DBSettings(BaseModel):
    url:str = DB_URL
    echo:bool = False
    
    
class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    
    
    
settings = Settings()