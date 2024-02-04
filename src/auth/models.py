from sqlalchemy import Column, VARCHAR
from src.models import Base
from shortuuid import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(VARCHAR(256), primary_key=True, index=True, default=uuid)
    username = Column(VARCHAR(256), unique=True, index=True, nullable=False)
    email = Column(VARCHAR(256), unique=True, index=True, nullable=False)
    hashed_password = Column(VARCHAR(256), index=False, unique=False, nullable=False)
