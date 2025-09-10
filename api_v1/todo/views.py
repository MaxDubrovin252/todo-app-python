from fastapi import APIRouter, Depends, Path, HTTPException
from typing import Annotated
from .schemas import TodoCreate, Todo, TodoUpdate
from . import crud
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import todo_by_id

router = APIRouter(prefix='/todo', tags=['todo'])



@router.post('/')
async def create_todo(todo:TodoCreate, session:AsyncSession = Depends(db_helper.session_dependecy)):
    new_todo = await crud.create(session=session, todo_in=todo)
    return {"id":new_todo.id}
    
    
    
@router.get('/{todo_id}')
async def get_todo(todo_id:Annotated [int,Path(ge=1)],session:AsyncSession = Depends(db_helper.session_dependecy)):
    return await crud.get_by_id(session=session, id=todo_id)



@router.get('/')
async def get_todos(session:AsyncSession = Depends(db_helper.session_dependecy)):
    return await crud.get_all(session=session)


@router.patch('/{todo_id}')
async def update_todo(todo_update:TodoUpdate,todo_id:Annotated[int,Path(ge=1)],session:AsyncSession = Depends(db_helper.session_dependecy)):
    return await crud.update(session=session, todo_id=todo_id, todo_update=todo_update)


@router.delete('/{todo_id}')
async def delete_todo(todo_id:Annotated[int, Path(ge=1)], session:AsyncSession = Depends(db_helper.session_dependecy)):
    status = await crud.delete(session=session, todo_id=todo_id)
    if status is False:
        return HTTPException(status_code=404, detail=f"todo with id {todo_id} not found")
    return {"status":"completed"}
    