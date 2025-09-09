from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import TodoCreate
from core.models import Todo


async def create(session:AsyncSession,todo_in:TodoCreate)->Todo:
    new_todo = Todo(**todo_in.model_dump())
    session.add(new_todo)
    await session.commit()
    return new_todo
