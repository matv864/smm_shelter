import uuid
import datetime

from src.database.core import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Pets(Base):
    __tablename__ = "pets"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    status: Mapped[str] = mapped_column(nullable=False)

    name: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)

    type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("pets_type.id"))

    date_birth: Mapped[datetime.datetime] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)

    breed: Mapped[str] = mapped_column(nullable=True)
    personality: Mapped[str] = mapped_column(nullable=True)
    appearance: Mapped[str] = mapped_column(nullable=True)
    health: Mapped[str] = mapped_column(nullable=True)

    description: Mapped[str] = mapped_column(nullable=True)

    images: Mapped[list["Images"]] = relationship(lazy="selectin")


class Pets_type(Base):
    __tablename__ = "pets_type"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)


class Images(Base):
    __tablename__ = "image"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    filename: Mapped[str] = mapped_column(nullable=False)
    pets_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("pets.id"))
