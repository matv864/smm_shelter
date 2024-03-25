from fastapi import FastAPI, APIRouter
# from fastapi.middleware.cors import CORSMiddleware
from src.auth_service.api import auth_router
from src.pets_service.api import joke_router
from src.calculator_service.api import calc_router

app = FastAPI(
    title="services",
)

# api = APIRouter(prefix="/api/v1")
# app.include_router(api)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(auth_router)
app.include_router(joke_router)
app.include_router(calc_router)
