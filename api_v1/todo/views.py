from fastapi import APIRouter, Depends, Path, HTTPException
from typing import Annotated
from .schemas import TodoCreate
from . import crud
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix='/todo', tags=['todo'])



@router.post('/')
async def create_todo(todo:TodoCreate, session:AsyncSession = Depends(db_helper.session_dependecy)):
    new_todo = await crud.create(session=session, todo_in=todo)
    return {"id":new_todo.id}
    
    
    
@router.get('/{todo_id}')
async def get_todo(todo_id:Annotated[int, Path(ge=1)], session:AsyncSession = Depends(db_helper.session_dependecy)):
    todo = await crud.get_by_id(session=session, id=todo_id)
    return todo


@router.get('/')
async def get_todos(session:AsyncSession = Depends(db_helper.session_dependecy)):
    return await crud.get_all(session=session)