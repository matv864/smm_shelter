import uuid
from typing import Optional

from pydantic import BaseModel


class Pets_type_insert_schema(BaseModel):
    name: str
    description: Optional[str] = None


class Pets_type_patch_schema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Pets_type_output_schema(BaseModel):
    id: uuid.UUID
    name: str
    description: Optional[str]
