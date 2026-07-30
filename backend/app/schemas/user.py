from pydantic import BaseModel, ConfigDict
from datetime import date

#Create the schema
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    date_of_birth: date 

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    model_config = ConfigDict(from_attributes=True)

class LoginResponse(BaseModel):
    access_token: str
    tokey_type: str