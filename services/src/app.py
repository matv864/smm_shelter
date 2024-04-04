from fastapi import FastAPI

from src.auth_service.api import auth_router
from src.pets_service.api.router import pets_service_router

app = FastAPI(
    title="services",
)

app.include_router(auth_router)
app.include_router(pets_service_router)
