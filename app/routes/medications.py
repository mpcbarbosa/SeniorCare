from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.medication import Medication
from ..models.user import User
from pydantic import BaseModel, ConfigDict
from datetime import time

router = APIRouter()

class MedicationCreate(BaseModel):
    name: str
    dose: str
    time: str  # HH:MM format
    frequency: str = "daily"

class MedicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    name: str
    dose: str
    time: str
    frequency: str

@router.post("/medications/", response_model=MedicationResponse)
def create_medication(medication: MedicationCreate, user_id: int, db: Session = Depends(get_db)):
    # Check if user exists
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Parse time
    try:
        parsed_time = time.fromisoformat(medication.time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format, use HH:MM")
    
    db_medication = Medication(
        user_id=user_id,
        name=medication.name,
        dose=medication.dose,
        time=parsed_time,
        frequency=medication.frequency
    )
    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)
    return db_medication

@router.get("/medications/{user_id}", response_model=list[MedicationResponse])
def read_medications(user_id: int, db: Session = Depends(get_db)):
    medications = db.query(Medication).filter(Medication.user_id == user_id).all()
    return medications

@router.put("/medications/{medication_id}", response_model=MedicationResponse)
def update_medication(medication_id: int, medication: MedicationCreate, db: Session = Depends(get_db)):
    db_medication = db.query(Medication).filter(Medication.id == medication_id).first()
    if not db_medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    
    try:
        parsed_time = time.fromisoformat(medication.time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format, use HH:MM")
    
    db_medication.name = medication.name
    db_medication.dose = medication.dose
    db_medication.time = parsed_time
    db_medication.frequency = medication.frequency
    db.commit()
    db.refresh(db_medication)
    return db_medication

@router.delete("/medications/{medication_id}")
def delete_medication(medication_id: int, db: Session = Depends(get_db)):
    db_medication = db.query(Medication).filter(Medication.id == medication_id).first()
    if not db_medication:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(db_medication)
    db.commit()
    return {"message": "Medication deleted"}