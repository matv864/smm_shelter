import uuid
import datetime

from src.database.core import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Pets(Base):
    __tablename__ = "pets"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    status: Mapped[str] = mapped_column(nullable=False)
    type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("pets_type.id"))
    date_birth: Mapped[datetime.datetime] = mapped_column(nullable=True)
    litter_box: Mapped[bool] = mapped_column(nullable=True)
    vaccinated: Mapped[bool] = mapped_column(nullable=True)
    castrated: Mapped[bool] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    images: Mapped[list["Images"]] = relationship(lazy="selectin")


class Pets_type(Base):
    __tablename__ = "pets_type"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)


class Images(Base):
    __tablename__ = "image"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    path: Mapped[str] = mapped_column(nullable=False)
    parent_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("pets.id"))
