from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import TodoCreate, TodoUpdate
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


async def update(session:AsyncSession, todo:Todo, todo_update:TodoUpdate):
    for title , description,status in todo_update.model_dump(exclude_none=True).items():
        setattr(todo, title, description, status)
    
    await session.commit()
    return todo


async def delete(session:AsyncSession, todo:Todo):
    await session.delete(todo)
    await session.commit()
    