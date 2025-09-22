from api_v1.auth.utils import verify_token
from fastapi import HTTPException




def user_verify_by_token(token:str):
    correct = verify_token(token)
    
    if correct is False:
        raise HTTPException(status_code=401, detail="failed to authorize")
    if correct is None:
        raise HTTPException(status_code=401, detail="token time expired")
    
    
    
    return correct