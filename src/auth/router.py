from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.schemas import Token, FullUserSchema, BasicUserSchema
from src.auth.jwt_handler import get_jwt
from src.database import get_db
from src.auth.dependencies import get_current_user, verify_user_signup_data
from src.auth.service import authenticate_user, create_user


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = get_jwt(user)
    return access_token


@router.post("/register", response_model=Token)
async def register_user(user: FullUserSchema = Depends(verify_user_signup_data), db: Session = Depends(get_db)):
    user = create_user(db, user)
    access_token = get_jwt(user)
    return access_token


@router.get("/me", response_model=BasicUserSchema)
async def read_users_me(current_user: FullUserSchema = Depends(get_current_user)):
    return BasicUserSchema(**current_user.dict())
