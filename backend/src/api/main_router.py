from fastapi import APIRouter, Request, status

from src.database import My_crud
from src.database import Pet

from .schemas import Pet_schema

main_pets_router = APIRouter()


@main_pets_router.get("/")
async def get_head(request: Request):
    return request.headers


@main_pets_router.get(
    "/pet/list",
    response_model=list[Pet_schema],
    status_code=status.HTTP_200_OK
)
async def all_pets(offset: int = 0, limit: int = 100):
    return My_crud(Pet).get(
        offset=offset,
        limit=limit,
        multi=True
    )


@main_pets_router.get(
    "/pet/{pets_id}",
    response_model=Pet_schema,
    status_code=status.HTTP_200_OK
)
async def get_pet(pets_id):
    return My_crud(Pet).get(filters=[Pet.id == pets_id])
