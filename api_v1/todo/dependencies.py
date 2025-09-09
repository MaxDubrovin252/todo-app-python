from fastapi import Depends, Path, HTTPException
from . import crud
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from typing import Annotated



async def todo_by_id(todo_id:Annotated[int, Path(ge=1)],session:AsyncSession = Depends(db_helper.session_dependecy)):
    todo = await crud.get_by_id(session=session, id=todo_id)
    if todo is None:
        HTTPException(status_code=404, detail=f"todo with id {todo_id} not found")