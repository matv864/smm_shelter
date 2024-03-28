from datetime import date
from typing import Optional, List

from pydantic import BaseModel


class Card_filter_schema(BaseModel):
    pet_type_id: Optional[int] = None
    castrated: Optional[bool] = None
    vaccinated: Optional[bool] = None
    cat_litter_box: Optional[bool] = None


class Update_card_schema(BaseModel):
    id: int
    pet_name: Optional[str] = None
    pet_type_id: Optional[int] = None
    date_birth: Optional[date] = None
    main_image: Optional[str] = None
    castrated: Optional[bool] = None
    vaccinated: Optional[bool] = None
    cat_litter_box: Optional[bool] = None
    description: Optional[str] = None


class Card_schema(BaseModel):
    id: Optional[int] = None
    pet_name: str
    pet_type: Optional["Pet_type_shema"] = None
    pet_type_id: int
    date_birth: Optional[date] = None
    main_image: Optional[str] = None
    castrated: Optional[bool] = None
    vaccinated: Optional[bool] = None
    cat_litter_box: Optional[bool] = None
    description: Optional[str] = None
    counter_views: int = 0
    donated_amount: int = 0


class Full_card_schema(Card_schema):
    articles: Optional[List["Article_schema"]] = None


class Article_schema(BaseModel):
    id: Optional[int] = None
    title: str
    body: Optional[str] = None
    date_publish: date
    card_id: int
    images: Optional[List["Image_schema"]] = None


class Pet_type_shema(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None


class Image_schema(BaseModel):
    id: Optional[int] = None
    filename: str
    article_id: int
