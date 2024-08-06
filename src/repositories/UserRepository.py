from ..config.DatabaseConnection import db, Database
from sqlalchemy import text

class UserRepository:
    def __init__(self):
        self._session = db.session

    async def obtain_user(self, id: int | str) -> list:
        result = list()
        try:
            query = "SELECT * FROM Test.Usuarios WHERE id = :id"
            data = self._session.execute(text(query), {"id": id})
            result = data.fetchall()
        except Exception as e:
            print(f"Error to select the user by id: {id}", e)
            self._session.rollback()
        finally:
            self._session.close()
            return result
