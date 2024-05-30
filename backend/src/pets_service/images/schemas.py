from typing import Optional
import uuid

from pydantic import BaseModel


class Images_record_schema(BaseModel):
    id: Optional[uuid.UUID] = None
    filename: str
    pets_id: uuid.UUID
