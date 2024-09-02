from uuid import UUID, uuid4

from sqladmin import ModelView

from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class ReportType(Base):
    __tablename__ = "reportType"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    type: Mapped[str]

    def __str__(self):
        return f"{self.type}"


class ReportTypeAdmin(ModelView, model=ReportType):
    name = "тип отчёта"
    name_plural = "типы отчётов"
    icon = "fa-solid fa-business-time"
    category = "отчёт"

    column_list = [
        ReportType.type
    ]

    column_searchable_list = [ReportType.type]
