import bcrypt

def hash_password(password:str)->bytes:
    return bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())

def verify_password(password:str, hash_pass:bytes)->bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hash_pass)