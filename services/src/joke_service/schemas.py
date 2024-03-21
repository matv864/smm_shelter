from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Joke_record(BaseModel):
    id: int
    title: Optional[str]
    theme: Optional[str]
    text_joke: str
    creating: Optional[datetime]


class Joke_creating(BaseModel):
    title: Optional[str]
    theme: Optional[str]
    text_joke: str
    creating: Optional[datetime]
