from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

from src.database import make_admin, unzip_storage
from src.api.main_router import main_pets_router

load_dotenv()

app = FastAPI(title="backend")
make_admin(app)
unzip_storage()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_pets_router)
