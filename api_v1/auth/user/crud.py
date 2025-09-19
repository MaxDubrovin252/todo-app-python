from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from sqlalchemy import select



async def create_user(session:AsyncSession,username:str, password:bytes)->User|None:
    stmt = select(User).where(User.username==username)
    res = await session.execute(statement=stmt)
    user_exist = res.scalars().first()
    
    if user_exist:
        await session.rollback()
        return None
    
    
    new_user = User(username=username, password=password)
    session.add(new_user)
    await session.commit()
    return new_user



async def get_user(session:AsyncSession, username:str)->User|None:
    stmt = select(User).where(User.username==username)
    res = await session.execute(statement=stmt)
    user_exist = res.scalars().first()
    
    if user_exist is None:
        await session.rollback()
        return None
    
    return user_exist