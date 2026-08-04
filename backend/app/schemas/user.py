from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import date

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    date_of_birth: date 

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    model_config = ConfigDict(from_attributes=True)

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    first_name: str
    last_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponsse(BaseModel):
    pass