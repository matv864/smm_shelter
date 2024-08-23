from uuid import UUID, uuid4

from sqladmin import ModelView

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Gender(Base):
    __tablename__ = "gender"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    name: Mapped[str]

    def __str__(self):
        return f"{self.name}"


class GenderAdmin(ModelView, model=Gender):
    name = "пол"
    name_plural = "пол"
    icon = "fa-solid fa-venus-mars"
    category = "база данных питомцев"

    column_list = [
        Gender.name
    ]
