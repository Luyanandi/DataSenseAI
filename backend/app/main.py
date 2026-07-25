from fastapi import FastAPI

app = FastAPI(title="DataSenseAI")

@app.get("/")
def root():
    return {"message": "Welcome to DataSenseAI API"}