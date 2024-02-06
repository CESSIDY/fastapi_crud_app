from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.database import get_db
from src.auth.schemas import UserSignupSchema, UserSchema, FullUserSchema
from src.auth.service import get_user_by_username, get_user_by_username_or_email
from src.auth.jwt_handler import verify_token
from src.auth.utils import get_password_hash

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> FullUserSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    print(token)
    user_schema: UserSchema = verify_token(token, credentials_exception)
    user: FullUserSchema = get_user_by_username(db, user_schema.username)
    return user


def verify_user_signup_data(user: UserSignupSchema, db: Session = Depends(get_db)) -> FullUserSchema:

    user_exists_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="user already exists",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_email_exists_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="user with current email already exists",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_username_exists_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="username is already taken",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_exists: FullUserSchema = get_user_by_username_or_email(db, user.username, user.email)
    if user_exists:
        if user.email == user_exists.email and user.username == user_exists.username:
            raise user_exists_exception
        if user.email == user_exists.email:
            raise user_email_exists_exception
        elif user.username == user_exists.username:
            raise user_username_exists_exception

    hashed_password = get_password_hash(user.password)
    return FullUserSchema(username=user.username, email=user.email, hashed_password=hashed_password)
