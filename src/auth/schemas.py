from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    username: str = Field()
    class Config:
        extra = "ignore"


class BasicUserSchema(UserSchema):
    email: EmailStr = Field(default=None)


class FullUserSchema(BasicUserSchema):
    hashed_password: str = Field(default=None)

    class Config:
        extra = "ignore"


class UserFromDBSchema(FullUserSchema):
    id: str = Field(default=None)

    class Config:
        extra = "ignore"


class UserSignupSchema(BasicUserSchema):
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "username": "Johnny Black",
                "email": "johnnyblack@some_host.com",
                "password": "somepassword"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "email": "johnnyblack@some_host.com",
                "password": "somepassword"
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: UserSchema
