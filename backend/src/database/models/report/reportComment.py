from uuid import UUID, uuid4
import datetime

from sqladmin import ModelView

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text

from ..base import Base


class ReportComment(Base):
    __tablename__ = "reportComment"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    date: Mapped[datetime.date] = mapped_column(default=datetime.date.today)
    text: Mapped[str] = mapped_column(Text, default="")
    type_id: Mapped[str] = mapped_column(ForeignKey("reportType.id"))
    type = relationship("ReportType", lazy="selectin")

    def __str__(self):
        return f"{self.date}"


class ReportCommentAdmin(ModelView, model=ReportComment):
    edit_template = "custom_edit.html"

    name = "комментарий для отчёта"
    name_plural = "комментарий для отчётов"
    icon = "fa-solid fa-keyboard"
    category = "отчёт"

    column_list = [
        ReportComment.date,
        ReportComment.type,
        ReportComment.text
    ]

    column_searchable_list = [ReportComment.text]
