from fastapi import FastAPI
from .database import engine
from .models import user, medication, routine  # Import models to create tables
from .routes import users, medications, routines, ai

user.Base.metadata.create_all(bind=engine)  # Create tables

app = FastAPI(title="SeniorCare API", version="1.0.0")

app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(medications.router, prefix="/api", tags=["medications"])
app.include_router(routines.router, prefix="/api", tags=["routines"])
app.include_router(ai.router, prefix="/api", tags=["ai"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SeniorCare API"}