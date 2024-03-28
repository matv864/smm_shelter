from fastapi import APIRouter

from src.pets_service.api.card import card_router
from src.pets_service.api.article import article_router
from src.pets_service.api.pet_type import pet_type_rounter

pets_service_router = APIRouter(prefix="/api/v1")

pets_service_router.include_router(card_router)
pets_service_router.include_router(article_router)
pets_service_router.include_router(pet_type_rounter)
