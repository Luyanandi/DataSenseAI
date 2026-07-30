from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin, LoginResponse
from app.services.user_services import register_user, login_user
from app.utils.security import create_access_token 

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

@router.post("/login", response_model=LoginResponse)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
    ):

    logged_in_user = login_user(user, db)

    access_token = create_access_token(
        data={"sub": str(logged_in_user.id)}
    )
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        first_name=logged_in_user.first_name,
        last_name=logged_in_user.last_name
    )