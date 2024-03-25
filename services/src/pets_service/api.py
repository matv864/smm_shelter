from fastapi import APIRouter, status, Depends

from src.pets_service.service.pet import Pets_service
# from src.pets_service.schemas import Joke_record, Joke_creating

from fastapi.security import OAuth2PasswordBearer

from typing import Annotated

joke_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@joke_router.get("/list")
async def get_list_of_pets():
    return await Pets_service().get_list_cards()


@joke_router.get("/{id}")
async def get_pet_by_id(id: int):
    return await Pets_service().get_card(id)


# @joke_router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_joke(
#     payload: Joke_creating,
#     token: Annotated[str, Depends(oauth2_scheme)]
# ):
#     return await Joke_service().create_joke(payload, token)


# @joke_router.put("/", status_code=status.HTTP_200_OK)
# async def update_joke(
#     payload: Joke_record,
#     token: Annotated[str, Depends(oauth2_scheme)]
# ):
#     return await Joke_service().update_joke(payload, token)


# @joke_router.delete("/{id}", status_code=status.HTTP_200_OK)
# async def dalete_by_id(
#     id: int,
#     token: Annotated[str, Depends(oauth2_scheme)]
# ):
#     return await Joke_service().delete_joke(id, token)
# ---------------------------------------------------------------------------------

# @events_router.get("/", response_model=list[GetEventList])
# async def listevents(
#     filter: Annotated[EventListFilterSchema, Depends(EventListFilterSchema)],
# ):
#     return await get_event_service().get_event_list(filter)

# @events_router.post("/register", response_model=RegistrationSchema)
# async def register_on_event(
#     register: PostRegister, authorization: Annotated[str, Header()]
# ):
    # return await get_registraton_service().regiser(
    #     register.ticket_id,
    #     authorization
    # )
