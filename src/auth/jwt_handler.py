from datetime import datetime, timedelta
from typing import Optional, Dict

import jwt

from src.config import settings
from src.auth.schemas import Token, TokenData, UserSchema

JWT_SECRET = settings.JWT_SECRET
JWT_ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def token_response(token: str) -> Token:
    return Token(access_token=token, token_type="bearer")


def sign_jwt(data: TokenData, expires_delta: Optional[timedelta] = None) -> Token:
    to_encode = data.dict()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(encoded_jwt)


def decode_jwt(token: str) -> TokenData | Dict:
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token['exp'] >= int(datetime.utcnow().timestamp()) else None
    except Exception as e:
        return {}


def verify_token(token, credentials_exception: Exception) -> UserSchema | Exception:
    payload = decode_jwt(token)
    username = payload.get('sub', {}).get('username')
    if not username:
        raise credentials_exception
    return UserSchema(username=username)

def get_jwt(sub_schema: UserSchema) -> Token:
    token_data = TokenData(sub=sub_schema)
    return sign_jwt(data=token_data)
