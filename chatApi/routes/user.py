from fastapi import APIRouter
from chatApi.models.user import UserMetaData
from chatApi.api.user import create_update_user

router = APIRouter()

@router.post("/user/")
async def create_update_user_endPoint(user: UserMetaData):
    return create_update_user(user)


