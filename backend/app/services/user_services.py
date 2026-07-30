from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password

def register_user(user: UserCreate, db: Session) -> User:
    existing_user = (
                    db.query(User)
                    .filter(User.email == user.email)
                    .first()
    )

    if existing_user:
        raise ValueError("Email already registered")
    
    hashed_password = hash_password(user.password)

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hashed_password,
        date_of_birth=user.date_of_birth
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user