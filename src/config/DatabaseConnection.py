from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from dotenv import load_dotenv
import os

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()

        return cls._instance
    
    def _initialize(self):
        load_dotenv()

        username = os.getenv("MSSQL_USERNAME")
        password = os.getenv("MSSQL_PASSWORD")
        database = os.getenv("MSSQL_DATABASE")
        server = os.getenv("MSSQL_SERVER")

        self._engine = create_engine(
            f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server",
            poolclass=QueuePool,
            pool_size=10,
            max_overflow=15
        )

        self._session_factory = sessionmaker(bind=self._engine)

    @property
    def session(self):
        return self._session_factory()
    
db = Database()