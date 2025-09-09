from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import TodoCreate
from core.models import Todo
from sqlalchemy import select,Result

async def create(session:AsyncSession,todo_in:TodoCreate)->Todo:
    new_todo = Todo(**todo_in.model_dump())
    session.add(new_todo)
    await session.commit()
    return new_todo


async def get_all(session:AsyncSession)->list[Todo]:
    stmt = select(Todo).order_by(Todo.id)
    result :Result = await session.execute(statement=stmt)
    todos = result.scalars().all()
    return list(todos)


async def get_by_id(session:AsyncSession, id:int)->Todo|None:
    stmt = select(Todo).where(Todo.id==id)
    result :Result = await session.execute(statement=stmt)
    todo = result.scalars().one()
    return todo