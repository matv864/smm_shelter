from typing import Optional, List
import uuid
import datetime

from pydantic import BaseModel


from src.pets_service.images.schemas import Images_record_schema


class Pets_insert_schema(BaseModel):
    name: str
    status: str
    gender: str
    type_id: uuid.UUID
    date_birth: Optional[datetime.datetime] = None
    age: Optional[int] = None
    litter_box: Optional[bool] = None
    vaccinated: Optional[bool] = None
    castrated: Optional[bool] = None
    description: Optional[str] = None


class Pets_patch_schema(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    type_id: Optional[uuid.UUID] = None
    date_birth: Optional[datetime.datetime] = None
    litter_box: Optional[bool] = None
    vaccinated: Optional[bool] = None
    castrated: Optional[bool] = None
    description: Optional[str] = None


class Pets_output_schema(BaseModel):
    id: uuid.UUID

    status: str

    name: str
    gender: str

    type_id: uuid.UUID

    date_birth: Optional[datetime.datetime]
    age: Optional[int]

    personality: Optional[str]
    appearance: Optional[str]
    health: Optional[str]

    images: List["Images_record_schema"]
