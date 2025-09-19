from fastapi import APIRouter, Depends, HTTPException
from .schemas import User
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from api_v1.auth.utils import hash_password
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/sign_up")
async def create_user(user:User, session:AsyncSession = Depends(db_helper.session_dependecy)):
    hash_pass = hash_password(password=user.password)
    return await crud.create_user(session=session, username=user.username, password=hash_pass)