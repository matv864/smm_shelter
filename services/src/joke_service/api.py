from fastapi import APIRouter, status

from src.joke_service.service.joke import Joke_service
from src.joke_service.schemas import Joke_record, Joke_creating


joke_router = APIRouter(
    prefix="/jokes",
)


@joke_router.get("/list", response_model=list[Joke_record])
async def get_list_of_jokes():
    return await Joke_service().get_list_jokes()


@joke_router.get("/{id}", response_model=Joke_record)
async def get_by_id(id: int):
    return await Joke_service().get_joke(id)


@joke_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_joke(payload: Joke_creating):
    return await Joke_service().create_joke(payload)


@joke_router.put("/", status_code=status.HTTP_200_OK)
async def update_joke(payload: Joke_record):
    return await Joke_service().update_joke(payload)


@joke_router.delete("/{id}", status_code=status.HTTP_200_OK)
async def dalete_by_id(id: int):
    return await Joke_service().delete_joke(id)


# @events_router.get("/", response_model=list[GetEventList])
# async def listevents(
#     filter: Annotated[EventListFilterSchema, Depends(EventListFilterSchema)],
# ):
#     return await get_event_service().get_event_list(filter)

# @events_router.post("/register", response_model=RegistrationSchema)
# async def register_on_event(
#     register: PostRegister, authorization: Annotated[str, Header()]
# ):
#     return await get_registraton_service().regiser(register.ticket_id, authorization)
