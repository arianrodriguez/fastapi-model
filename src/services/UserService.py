from ..repositories.UserRepository import UserRepository

class UserService:
    def __init__(self):
        self._repository = UserRepository()

    async def obtain_user(self, id: int | str) -> list:
        return await self._repository.obtain_user(id)