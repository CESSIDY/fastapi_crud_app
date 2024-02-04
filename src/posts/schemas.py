from pydantic import BaseModel


class BasePost(BaseModel):
    title: str
    content: str


class PostCreate(BasePost):
    pass


class PostShow(BasePost):
    id: int
