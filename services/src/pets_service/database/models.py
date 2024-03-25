from sqlalchemy.ext.asyncio import AsyncAttrs

from datetime import date
from typing import List

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(
    AsyncAttrs, DeclarativeBase
):
    pass


class Card(Base):
    __tablename__ = "card"

    id: Mapped[int] = mapped_column(primary_key=True)
    pet_name: Mapped[str] = mapped_column()
    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_type.id"))
    date_birth: Mapped[date] = mapped_column(DateTime(timezone=True))
    castrated: Mapped[bool] = mapped_column()
    vaccinated: Mapped[bool] = mapped_column()
    cat_litter_box: Mapped[bool] = mapped_column()
    description: Mapped[str] = mapped_column()
    counter_views: Mapped[int] = mapped_column(default=0)
    donated_amount: Mapped[int] = mapped_column(default=0)

    pet_type: Mapped["Pet_type"] = relationship()
    articles: Mapped[List["Article"]] = relationship()


class Article(Base):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column()
    date_publish: Mapped[date] = mapped_column()
    card_id: Mapped[int] = mapped_column(ForeignKey("card.id"))

    images: Mapped[List["Image"]] = relationship()


class Pet_type(Base):
    __tablename__ = "pet_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column()
    article_id: Mapped[int] = mapped_column(ForeignKey("article.id"))
