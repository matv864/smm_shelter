from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from src.auth_service.api import auth_router
from src.joke_service.api import joke_router

app = FastAPI(
    title="services",
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(auth_router)
app.include_router(joke_router)
