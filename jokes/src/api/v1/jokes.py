from fastapi import APIRouter, status

from src.service.joke import Joke_service
from src.schemas.joke import Joke_record, Joke_payload


events_router = APIRouter(
    prefix="/jokes",
)


@events_router.get("/list", response_model=list[Joke_record])
async def get_list_of_jokes():
    return await Joke_service().get_list_jokes()


@events_router.get("/{id}", response_model=Joke_record)
async def get_by_id(id: int):
    return await Joke_service().get_joke(id)


@events_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_joke(payload: Joke_payload):
    return await Joke_service().create_joke(payload)


@events_router.put("/", status_code=status.HTTP_200_OK)
async def update_joke(payload: Joke_record):
    print(payload)
    return await Joke_service().update_joke(payload)


@events_router.delete("/{id}", status_code=status.HTTP_200_OK)
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
