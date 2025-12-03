from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Import here to avoid import time issues
    from app.database import get_engine
    from app.models import user, medication, routine  # Import models to create tables
    # Create tables on startup
    user.Base.metadata.create_all(bind=get_engine())
    yield

app = FastAPI(title="SeniorCare API", version="1.0.0", lifespan=lifespan)

# Import routes after app definition
from app.routes import users, medications, routines, ai

app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(medications.router, prefix="/api", tags=["medications"])
app.include_router(routines.router, prefix="/api", tags=["routines"])
app.include_router(ai.router, prefix="/api", tags=["ai"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SeniorCare API"}

application = app