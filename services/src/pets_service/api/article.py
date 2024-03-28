from typing import Annotated

from fastapi import APIRouter, status, Depends


from src.pets_service.service.article import Article_service
from src.pets_service.schemas import (
    Article_schema,
    Update_article_schema
)

from fastapi.security import OAuth2PasswordBearer
from src.security_module.jwt import verify_jwt_token


article_router = APIRouter(tags=["article"])


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@article_router.post("/create_article", status_code=status.HTTP_201_CREATED)
async def create_article(
    payload: Article_schema,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    await verify_jwt_token(token)
    return await Article_service().create_article(payload)


@article_router.put("/update_article", status_code=status.HTTP_200_OK)
async def update_article(
    payload: Annotated[Update_article_schema, Depends(Update_article_schema)],
    token: Annotated[str, Depends(oauth2_scheme)]
):
    await verify_jwt_token(token)
    return await Article_service().update_article(payload)


@article_router.delete("/delete_article/{id}", status_code=status.HTTP_200_OK)
async def delete_article(
    id: int,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    await verify_jwt_token(token)
    return await Article_service().delete_article(id)
