import jwt 
from datetime import datetime, timedelta
import os
from core import settings

def create_access_token(username:str,user_id:int, exp_time=1):
    payload:dict = {
        "sub":username,
        "exp": datetime.utcnow() + timedelta(hours=os.getenv("ACCESS_TOKEN_EXP")),
        "user_id":user_id,
        "iat":datetime.utcnow(),
    }
    
    token = jwt.encode(payload,settings.jwt.secret_key, settings.jwt.algo)
    return token


def verify_token(token):
    try:
        decoded_payload = jwt.decode(token, settings.jwt.secret_key,algorithms=os.getenv("ALGO"))
        return decoded_payload
    except jwt.InvalidTokenError:
        return False
    except jwt.ExpiredSignatureError:
        return None