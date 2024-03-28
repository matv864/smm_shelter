from typing import Annotated, List

from fastapi import APIRouter, status, Depends


from src.pets_service.service.pet_type import Pet_type_service
from src.pets_service.schemas import (
    Pet_type_shema
)

from fastapi.security import OAuth2PasswordBearer
from src.security_module.jwt import verify_jwt_token


pet_type_rounter = APIRouter(tags=["pet_type"])


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@pet_type_rounter.get("/list_types", response_model=List[Pet_type_shema])
async def get_list_pet_types():
    return await Pet_type_service().get_list_pet_types(filter)


@pet_type_rounter.post("/create_type_pet", status_code=status.HTTP_201_CREATED)
async def create_pet_type(
    payload: Pet_type_shema,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    await verify_jwt_token(token)
    return await Pet_type_service().create_pet_type(payload)


@pet_type_rounter.delete("/delete_type/{id}", status_code=status.HTTP_200_OK)
async def delete_pet_type(
    id: int,
    token: Annotated[str, Depends(oauth2_scheme)]
):
    await verify_jwt_token(token)
    return await Pet_type_service().delete_pet_type(id)
