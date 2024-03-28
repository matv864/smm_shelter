from fastapi import APIRouter

from src.pets_service.api.card import card_router

pets_service_router = APIRouter(prefix="/api/v1")

pets_service_router.include_router(card_router)
