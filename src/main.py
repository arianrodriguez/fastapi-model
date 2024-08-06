from fastapi import FastAPI
from .routes.ObtainUserData import router as route_user

app = FastAPI()

app.include_router(route_user)