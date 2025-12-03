from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

Base = declarative_base()

def get_engine():
    if not hasattr(get_engine, '_engine'):
        get_engine._engine = create_engine(settings.database_url)
    return get_engine._engine

def get_db():
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()