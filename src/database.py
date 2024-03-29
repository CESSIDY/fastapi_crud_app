from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from src.utils import mysql_connection_string


Base: DeclarativeMeta = declarative_base()

engine = create_engine(mysql_connection_string())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Base.metadata.create_all(bind=engine)
