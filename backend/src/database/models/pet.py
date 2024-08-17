from uuid import UUID, uuid4
from datetime import date

from sqladmin import ModelView

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Pet(Base):
    __tablename__ = "pet"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid4
    )
    status_id: Mapped[str] = mapped_column(ForeignKey("status.id"))
    status = relationship("Status")

    name: Mapped[str]

    gender_id: Mapped[str] = mapped_column(ForeignKey("gender.id"))
    gender = relationship("Gender")

    type_id: Mapped[str] = mapped_column(ForeignKey("petType.id"))
    type_name = relationship("PetType")

    date_birth: Mapped[date] = mapped_column(nullable=True)

    breed: Mapped[str] = mapped_column(nullable=True)
    personality: Mapped[str] = mapped_column(nullable=True)
    appearance: Mapped[str] = mapped_column(nullable=True)
    health: Mapped[str] = mapped_column(nullable=True)

    description: Mapped[str] = mapped_column(nullable=True)

    image = relationship(
        "Image",
        back_populates="pet",
        lazy="selectin"
    )

    def __str__(self):
        return f"{self.name}"


class PetAdmin(ModelView, model=Pet):
    name = "pet"
    name_plural = "pets"
    icon = "fa-solid fa-paw"

    column_list = [
        Pet.status,
        Pet.name,
        Pet.gender,
        Pet.type_name,
        Pet.date_birth,
        Pet.breed,
        Pet.personality,
        Pet.appearance,
        Pet.health,
        Pet.description
    ]
    form_excluded_columns = [
        Pet.image
    ]

    column_searchable_list = [Pet.name]
