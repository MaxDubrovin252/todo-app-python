from fastapi import Depends, Path
from . import crud
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from typing import Annotated



async def todo_by_id(todo_id:Annotated[int, Path(ge=1)],session:AsyncSession = Depends(db_helper.session_dependecy)):
    return await crud.get_by_id(session=session,id=todo_id )