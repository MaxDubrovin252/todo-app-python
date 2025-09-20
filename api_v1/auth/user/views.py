from fastapi import APIRouter, Depends, HTTPException
from .schemas import User
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from api_v1.auth.utils import hash_password, verify_password, create_access_token
from .dependencies import user_verify_by_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/sign_up")
async def sign_up(user:User, session:AsyncSession = Depends(db_helper.session_dependecy)):
    hash_pass = hash_password(password=user.password)
    new_user = await crud.create_user(session=session, username=user.username, password=hash_pass)
    if new_user is None:
        raise HTTPException(status_code=400,detail=f"user {user.username} is already login")
    return {"new user add":new_user.username}


@router.post("/sign_in")
async def sign_in(user:User,session:AsyncSession = Depends(db_helper.session_dependecy)):
    user_in = await crud.get_user(session=session, username=user.username)
    if user_in is None:
        raise HTTPException(status_code=404,detail="user not found")
    is_correct = verify_password(password=user.password, hash_pass=user_in.password)
    
    if is_correct is True:
        token = create_access_token(username=user.username,user_id=user_in.id)
        return {"token":token}
    
    if is_correct is False:
        raise HTTPException(status_code=400, detail="password is invalid")
    
    
