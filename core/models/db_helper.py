from sqlalchemy.ext.asyncio import async_sessionmaker , create_async_engine
from core import settings


class DBHelper:
    def __init__(self, url:str, echo:bool):
        self.engine = create_async_engine(
            url=url, 
            echo=echo,
        )
        
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
        
        
    async def session_dependecy(self):
        async with self.session_factory() as session:
            yield session
            await session.close()