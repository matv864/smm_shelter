from typing import Annotated, List

from fastapi import APIRouter, status, Depends


from src.pets_service.service.card import Card_service
from src.pets_service.schemas import (
    Card_schema,
    Full_card_schema,
    Update_card_schema,
    Card_filter_schema
)

from fastapi.security import OAuth2PasswordBearer
from src.security_module.jwt import verify_jwt_token


card_router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@card_router.post("/list", response_model=List[Card_schema])
async def get_list_of_cards(
    filter: Annotated[Card_filter_schema, Depends(Card_filter_schema)]
):
    return await Card_service().get_list_cards(filter)


@card_router.get("/{id}", response_model=Full_card_schema)
async def get_card_by_id(id: int):
    return await Card_service().get_card(id)


@card_router.post("/create_card", status_code=status.HTTP_201_CREATED)
async def create_card(
    payload: Card_schema,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    verify_jwt_token(token)
    return await Card_service().create_card(payload)


@card_router.put("/update_card", status_code=status.HTTP_200_OK)
async def update_card(
    payload: Annotated[Update_card_schema, Depends(Update_card_schema)],
    token: Annotated[str, Depends(oauth2_scheme)]
):
    print("---\n" * 10)
    verify_jwt_token(token)
    return await Card_service().update_card(payload)


@card_router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
async def delete_card_by_id(
    id: int,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    verify_jwt_token(token)
    return await Card_service().delete_card(id)
