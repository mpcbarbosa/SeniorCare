from fastapi import FastAPI
from .database import engine
from .models import user  # Import models to create tables
from .routes import users

user.Base.metadata.create_all(bind=engine)  # Create tables

app = FastAPI(title="SeniorCare API", version="1.0.0")

app.include_router(users.router, prefix="/api", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SeniorCare API"}