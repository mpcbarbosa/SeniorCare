from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.routine import Routine
from ..models.user import User
from pydantic import BaseModel
from datetime import time

router = APIRouter()

class RoutineCreate(BaseModel):
    activity: str
    time: str  # HH:MM format
    frequency: str = "daily"

class RoutineResponse(BaseModel):
    id: int
    user_id: int
    activity: str
    time: str
    frequency: str

    class Config:
        orm_mode = True

@router.post("/routines/", response_model=RoutineResponse)
def create_routine(routine: RoutineCreate, user_id: int, db: Session = Depends(get_db)):
    # Check if user exists
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Parse time
    try:
        parsed_time = time.fromisoformat(routine.time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format, use HH:MM")
    
    db_routine = Routine(
        user_id=user_id,
        activity=routine.activity,
        time=parsed_time,
        frequency=routine.frequency
    )
    db.add(db_routine)
    db.commit()
    db.refresh(db_routine)
    return db_routine

@router.get("/routines/{user_id}", response_model=list[RoutineResponse])
def read_routines(user_id: int, db: Session = Depends(get_db)):
    routines = db.query(Routine).filter(Routine.user_id == user_id).all()
    return routines

@router.put("/routines/{routine_id}", response_model=RoutineResponse)
def update_routine(routine_id: int, routine: RoutineCreate, db: Session = Depends(get_db)):
    db_routine = db.query(Routine).filter(Routine.id == routine_id).first()
    if not db_routine:
        raise HTTPException(status_code=404, detail="Routine not found")
    
    try:
        parsed_time = time.fromisoformat(routine.time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format, use HH:MM")
    
    db_routine.activity = routine.activity
    db_routine.time = parsed_time
    db_routine.frequency = routine.frequency
    db.commit()
    db.refresh(db_routine)
    return db_routine

@router.delete("/routines/{routine_id}")
def delete_routine(routine_id: int, db: Session = Depends(get_db)):
    db_routine = db.query(Routine).filter(Routine.id == routine_id).first()
    if not db_routine:
        raise HTTPException(status_code=404, detail="Routine not found")
    db.delete(db_routine)
    db.commit()
    return {"message": "Routine deleted"}