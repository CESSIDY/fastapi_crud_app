from fastapi.routing import APIRouter
from fastapi import Depends

router = APIRouter(
    prefix="/post",
    tags=["post"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_posts():
    return ""


