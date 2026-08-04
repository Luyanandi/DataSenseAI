from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone 
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User
from sqlalchemy.orm import Session
from app.database.database import get_db

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

SECRET_KEY = 'your-secret-key'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(plain_password: str):
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password
)

def create_access_token(data: dict): 
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("sub") is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = verify_access_token(token)
    user_id =payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials"
        )
    user = get_user_by_id(int(user_id),db)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials"
        )
    return user
    

def get_user_by_id(user_id: int, db: Session):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )