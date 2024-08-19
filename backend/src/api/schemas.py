from typing import Optional
from uuid import UUID
import datetime

from pydantic import BaseModel


class Pet_schema(BaseModel):
    id: UUID
    name: str

    type_name: "PetType"
    status: "Status"
    gender: "Gender"

    year_birth: Optional[datetime.datetime] = None

    description: Optional[str] = None

    image: list["Image"]


class Image(BaseModel):
    id: UUID
    filename: str
    pet_id: UUID


class Gender(BaseModel):
    id: UUID
    name: str


class Status(BaseModel):
    id: UUID
    name: str


class PetType(BaseModel):
    id: UUID
    name: str
