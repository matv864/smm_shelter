from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.pets_service.router import main_pets_router

app = FastAPI(title="backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_pets_router)
