from fastapi import APIRouter
from ..services.UserService import UserService

router = APIRouter()

@router.get("/users/{id}", tags=["Users"])
async def obtain_user_by_id(id: int | str):
    service = UserService()
    return await service.obtain_user(id)
