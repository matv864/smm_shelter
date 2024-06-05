from typing import Optional
import uuid
import datetime

from pydantic import BaseModel


class Pets_insert_schema(BaseModel):
    name: str
    status: str
    type_id: uuid.UUID
    date_birth: Optional[datetime.datetime] = None
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
    name: str
    status: str
    type_id: uuid.UUID
    date_birth: Optional[datetime.datetime]
    litter_box: Optional[bool]
    vaccinated: Optional[bool]
    castrated: Optional[bool]
    description: Optional[str]
    images: list
