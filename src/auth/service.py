from src.auth.schemas import FullUserSchema, UserSchema

from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.auth.models import User
from src.auth.utils import verify_password


def get_user_by_email(db: Session, email: str) -> FullUserSchema | None:
    user = db.query(User).filter(User.email == email).first()
    if user:
        return FullUserSchema(username=user.username, email=user.email, hashed_password=user.hashed_password)
    return


def get_user_by_username(db: Session, username: str) -> FullUserSchema | None:
    user = db.query(User).filter(User.username == username).first()
    if user:
        return FullUserSchema(username=user.username, email=user.email, hashed_password=user.hashed_password)
    return


def get_user_by_username_or_email(db: Session, username: str, email: str) -> FullUserSchema | None:
    user = db.query(User).filter(or_(
        User.username == username,
        User.email == email
    )).first()
    if user:
        return FullUserSchema(username=user.username, email=user.email, hashed_password=user.hashed_password)
    return


def authenticate_user(db: Session, username: str, password: str) -> UserSchema | None:
    user = get_user_by_username(db, username)
    if user and verify_password(password, user.hashed_password):
        return UserSchema(username=user.username)
    return None


def create_user(db: Session, user: FullUserSchema) -> UserSchema:
    db_user = User(username=user.username, email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    #db.refresh(db_user)#
    return UserSchema(username=db_user.username)
