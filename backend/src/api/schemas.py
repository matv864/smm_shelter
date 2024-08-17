from typing import Optional
from uuid import UUID, uuid4
import datetime

from pydantic import BaseModel


class Pet_schema(BaseModel):
    id: UUID
    name: str
    gender: str
    status: str
    type_name: str

    date_birth: Optional[datetime.datetime] = None

    breed: Optional[str] = None
    personality: Optional[str] = None
    appearance: Optional[str] = None
    health: Optional[str] = None

    description: Optional[str] = None

    image: list
