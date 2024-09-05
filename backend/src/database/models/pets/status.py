from uuid import UUID, uuid4

from sqladmin import ModelView

from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class Status(Base):
    __tablename__ = "status"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    name: Mapped[str]

    def __str__(self):
        return f"{self.name}"


class StatusAdmin(ModelView, model=Status):
    name = "статус питомца"
    name_plural = "статусы питомцев"
    icon = "fa-solid fa-house"
    category = "база данных питомцев"

    column_list = [
        Status.name
    ]

    column_searchable_list = [Status.name]
