from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from .schemas import TodoCreate, TodoUpdate, TodoUpdateAll
from core.models import Todo
from sqlalchemy import select,Result

async def create(session:AsyncSession,title:str, description:str, user_id:int,status:str = "not-complete")->Todo:
    new_todo = Todo(title=title, description=description,status=status,user_id=user_id)
    session.add(new_todo)
    await session.commit()
    return new_todo


async def get_all(session:AsyncSession, user_id:int)->list[Todo]:
    
    stmt = select(Todo).where(Todo.user_id==user_id)
    result :Result = await session.execute(statement=stmt)
    todos = result.scalars().all()
    return list(todos)


async def get_by_id(session:AsyncSession,todo_id:int)->Todo|None:
    
    
    stmt = select(Todo).where(Todo.id==todo_id)

    result :Result = await session.execute(statement=stmt)
    todo= result.scalars().first()
    return todo
    


async def update(session:AsyncSession, todo_id:int, todo_update:TodoUpdate):
    
    stmt = select(Todo).where(Todo.id==todo_id)
    res:Result = await session.execute(statement=stmt)
    todo = res.scalars().first()
    
    if todo is None:
        return None
    for name,value in todo_update.model_dump(exclude_none=True).items():
        setattr(todo, name, value)
    return todo


async def update_all(session:AsyncSession, todo_id:int, todo_update:TodoUpdateAll):
    stmt = select(Todo).where(Todo.id== todo_id)
    res:Result = await session.execute(statement=stmt)
    todo = res.scalars().one()

    if todo is None:
        return None
    
    for name,value in todo_update.model_dump().items():
        setattr(todo, name, value)
        
        
    await session.commit()
    
    return todo


async def delete(session:AsyncSession, todo_id:int)->bool:
    
        stmt = select(Todo).where(Todo.id== todo_id)
        result:Result = await session.execute(statement=stmt)
        todo = result.scalars().first()
    
        if todo is None:
            return False
        
        await session.delete(todo)
        await session.commit()

        return True



async def set_complete(session:AsyncSession, todo_id:int,complete:bool)->bool|None:
    stmt = select(Todo).where(Todo.id==todo_id)
    todo = await session.scalar(stmt)
    
    if todo is None:
        return False
    
    if complete is True:
        todo.status == "complete"
        return True
    
    return None
    