from fastapi import APIRouter, Depends
from .schemas import TodoCreate
from . import crud
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix='/todo', tags=['todo'])



@router.post('/create')
async def create_todo(todo:TodoCreate, session:AsyncSession = Depends(db_helper.session_dependecy)):
    new_todo = await crud.create(session=session, todo_in=todo)
    return new_todo
    