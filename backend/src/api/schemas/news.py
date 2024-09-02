from uuid import UUID
from datetime import date

from pydantic import BaseModel


class News_schema(BaseModel):
    id: UUID
    date_of_publication: date
    title: str
    text: str
    newsImage: list["NewsImage_schema"]


class NewsImage_schema(BaseModel):
    filename: str
