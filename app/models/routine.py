from sqlalchemy import Column, Integer, String, Time, DateTime, ForeignKey
from sqlalchemy.sql import func
from ..database import Base

class Routine(Base):
    __tablename__ = "routines"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    activity = Column(String, nullable=False)
    time = Column(Time, nullable=False)
    frequency = Column(String, default="daily")  # daily, weekly, etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())