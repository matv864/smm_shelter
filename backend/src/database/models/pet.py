import uuid
import datetime

from sqladmin import ModelView

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Pet(Base):
    __tablename__ = "pet"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    status: Mapped[str]

    name: Mapped[str]
    gender: Mapped[str]

    type_name: Mapped[str]

    date_birth: Mapped[datetime.datetime] = mapped_column(nullable=True)

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
    column_list = [
        Pet.id,
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
