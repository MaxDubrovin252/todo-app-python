from fastapi import APIRouter, Depends, Path, HTTPException,Form
from typing import Annotated
from .schemas import TodoCreate, Todo as todoSchema, TodoUpdate, TodoUpdateAll
from . import crud
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.auth.user.dependencies import user_verify_by_token



router = APIRouter(prefix='/todo', tags=['todo'])


@router.post("/set-complete/{todo_id}")
async def set_comp(todo_id:Annotated[int,Path(ge=1)],complete:bool= Form(), token:str=Depends(user_verify_by_token), session:AsyncSession = Depends(db_helper.session_dependecy)):
    status = await crud.set_complete(session=session,todo_id=todo_id, complete=complete)
    if status is False:
        raise HTTPException(status_code=404, detail=f"todo with id {todo_id} not found")
    return {"complete":status}

@router.post('/')
async def create_todo(todo:TodoCreate, token:str =Depends(user_verify_by_token),session:AsyncSession = Depends(db_helper.session_dependecy)):
    user_id = token["user_id"]
    new_todo = await crud.create(session=session,title=todo.title, description=todo.description, user_id=user_id)
    return {
        "message":"new todo created",
        "title":new_todo.title,
        "id":new_todo.id,
    }
    
    
    
@router.get('/{todo_id}')
async def get_todo(todo_id:Annotated[int, Path(ge=1)],token:str =Depends(user_verify_by_token),session:AsyncSession = Depends(db_helper.session_dependecy)):
    username = token["sub"]
    todo = await crud.get_by_id(session=session,todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"cannot found todo with id{todo_id}")
    todoShow = todoSchema(title=todo.title, description=todo.description, status=todo.status)
    
    
    return {f"{username}s todo":todoShow}



@router.get('/')
async def get_todos(token:str =Depends(user_verify_by_token),session:AsyncSession = Depends(db_helper.session_dependecy)):
    user_id = token["user_id"]
    username = token["sub"]
    todos = await crud.get_all(session=session, user_id=user_id)
    return {f"todo list of {username}":todos}


@router.patch('/{todo_id}')
async def update_todo(todo_update:TodoUpdate ,todo_id:Annotated[int,Path(ge=1)],token:str =Depends(user_verify_by_token),session:AsyncSession = Depends(db_helper.session_dependecy)):
    update_todo = await crud.update(session=session, todo_id=todo_id, todo_update=todo_update)
    if update_todo is None:
        raise HTTPException(status_code=404, detail=f"cannot found todo with id {todo_id}")
    return {"updated_todo":update_todo}


@router.put('/{todo_id}')
async def update_todo_all(todo_id:Annotated[int,Path(ge=1)],todo_update:TodoUpdateAll, token:str =Depends(user_verify_by_token),session:AsyncSession= Depends(db_helper.session_dependecy)):
    new_todo = await crud.update_all(session=session, todo_update=todo_update, todo_id=todo_id)
    if new_todo is None:
        HTTPException(status_code=404, detail=f"cannot found todo with id {todo_id}")
    return {"updated_todo":new_todo}

@router.delete('/{todo_id}')
async def delete_todo(todo_id:Annotated[int, Path(ge=1)], token:str=Depends(user_verify_by_token),session:AsyncSession = Depends(db_helper.session_dependecy)):
    status = await crud.delete(session=session, todo_id=todo_id)
    if status is False:
        raise HTTPException(status_code=404, detail=f"todo with id {todo_id} not found")
    return {"status":"completed"}





