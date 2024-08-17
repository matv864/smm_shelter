from uuid import UUID, uuid4

from sqladmin import ModelView

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PetType(Base):
    __tablename__ = "petType"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid4
    )

    name: Mapped[str]

    def __str__(self):
        return f"{self.name}"


class PetTypeAdmin(ModelView, model=PetType):
    name = "type of pet"
    name_plural = "types of pets"
    icon = "fa-solid fa-book"

    column_list = [
        PetType.name
    ]
