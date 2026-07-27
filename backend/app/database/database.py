from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

#Creat the SQLAlchemy engine
engine = create_engine(DATABASE_URL) 

#Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush= False,
    bind=engine
)

#base class for all models
Base = declarative_base()

#dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()