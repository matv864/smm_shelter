from sqlalchemy.ext.asyncio import AsyncAttrs

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(
    AsyncAttrs, DeclarativeBase
):
    pass


class Joke(Base):
    __tablename__ = "joke"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    theme: Mapped[str] = mapped_column()
    text_joke: Mapped[str] = mapped_column()
    creating: Mapped[datetime] = mapped_column(DateTime(timezone=True))
