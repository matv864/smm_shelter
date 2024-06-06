from fastapi import APIRouter

from src.pets_service.pets import pets_router
from src.pets_service.pets_type import pets_type_router
from src.pets_service.images import images_router

main_pets_router = APIRouter(prefix="/api")

main_pets_router.include_router(pets_router)
main_pets_router.include_router(pets_type_router)
main_pets_router.include_router(images_router)
