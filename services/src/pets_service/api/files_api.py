from typing import Annotated

from fastapi import APIRouter, status, Depends, Form, UploadFile

from src.pets_service.service.files import File_service

from fastapi.security import OAuth2PasswordBearer
from src.security_module.jwt import verify_jwt_token

file_router = APIRouter(tags=["file_api"])


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@file_router.post("/upload_main_image", status_code=status.HTTP_200_OK)
async def upload_main_image(
    id: Annotated[int, Form()],
    file: UploadFile,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    await verify_jwt_token(token)
    return await File_service().upload_main_image(id, file)


@file_router.post("/upload_article_image", status_code=status.HTTP_200_OK)
async def upload_article_image(
    card_id: Annotated[int, Form()],
    article_id: Annotated[int, Form()],
    file: UploadFile,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    await verify_jwt_token(token)
    return await File_service().upload_article_image(card_id, article_id, file)


@file_router.delete("/delete_article_image", status_code=status.HTTP_200_OK)
async def delete_article_image(
    card_id: int,
    image_id: int,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    await verify_jwt_token(token)
    return await File_service().delete_image(card_id, image_id)


@file_router.get("/get_main_image")
async def get_main_image(card_id: int):
    return await File_service().get_main_image(card_id)


@file_router.get("/get_article_image")
async def get_article_image(card_id: int, image_id: int):
    return await File_service().get_article_image(card_id, image_id)
