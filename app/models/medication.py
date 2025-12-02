from sqlalchemy import Column, Integer, String, Time, DateTime, ForeignKey
from sqlalchemy.sql import func
from ..database import Base

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    dose = Column(String, nullable=False)
    time = Column(Time, nullable=False)
    frequency = Column(String, default="daily")  # daily, weekly, etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())