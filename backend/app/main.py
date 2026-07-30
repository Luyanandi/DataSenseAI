from fastapi import FastAPI

from app.database.database import Base, engine
import app.models.user 
from app.routers.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DataSenseAI")
app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

@app.get("/")
def root():
    return {
        "message": "Welcome to DataSenseAI API"
        }