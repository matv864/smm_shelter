from uuid import UUID, uuid4
from datetime import date

from sqladmin import ModelView

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text

from ..base import Base


class News(Base):
    __tablename__ = "news"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    date_of_publication: Mapped[date] = mapped_column(default=date.today())

    title: Mapped[str]
    text: Mapped[str] = mapped_column(Text, default="")

    newsImage = relationship(
        "NewsImage",
        back_populates="news",
        lazy="selectin"
    )

    def __str__(self):
        return f"{self.title}"


class NewsAdmin(ModelView, model=News):
    edit_template = "custom_edit.html"

    name = "новость"
    name_plural = "новости"
    icon = "fa-solid fa-newspaper"
    category = "новости"

    column_list = [
        News.date_of_publication,
        News.title,
        News.text
    ]
    form_excluded_columns = [
        News.newsImage
    ]

    column_searchable_list = [News.title]
