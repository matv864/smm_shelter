from typing import Optional
from uuid import UUID
from datetime import date

from pydantic import BaseModel


class Pet_schema(BaseModel):
    id: UUID
    name: str

    type: "PetType_schema"
    status: "PetStatus_schema"
    gender: "Gender_schema"

    year_birth: Optional[date] = None
    in_shelter_from: Optional[date] = None

    description: Optional[str]

    article: list["Article_schema"]
    petImage: list["PetImage_schema"]


class Pets_schema(BaseModel):
    id: UUID
    name: str

    type: "PetType_schema"
    status: "PetStatus_schema"
    gender: "Gender_schema"

    year_birth: Optional[date] = None
    in_shelter_from: Optional[date] = None

    description: Optional[str]

    petImage: list["PetImage_schema"]


class Article_schema(BaseModel):
    date: date
    title: str
    text: str


class PetImage_schema(BaseModel):
    filename: str


class Gender_schema(BaseModel):
    name: str


class PetStatus_schema(BaseModel):
    name: str


class PetType_schema(BaseModel):
    name: str
