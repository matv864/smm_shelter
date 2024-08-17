from typing import Optional
import uuid
import datetime

from pydantic import BaseModel


class Pet_schema(BaseModel):
    id: uuid.UUID
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
