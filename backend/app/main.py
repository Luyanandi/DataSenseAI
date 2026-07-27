from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DataSenseAI")


@app.get("/")
def root():
    return {"message": "Welcome to DataSenseAI API"}