from pydantic_settings import BaseSettings
from pydantic import BaseModel



class DBSettings(BaseModel):
    url:str = "postgresql+asyncpg://myuser:mypassword@localhost:5432/mydb"
    echo:bool = False
    
    
class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    
    
    
settings = Settings()