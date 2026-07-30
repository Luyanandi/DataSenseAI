from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_services import register_user

router = APIRouter() 

@router.post("/register", response_model=UserResponse)
def register(
    user:UserCreate,
    db:Session = Depends(get_db)
):
    try:
        new_user = register_user(user, db)
        return new_user
    except ValueError as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )