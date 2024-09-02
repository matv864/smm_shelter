from uuid import UUID, uuid4
import datetime

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqladmin import ModelView

from ..base import Base


class Article(Base):
    __tablename__ = "article"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    date: Mapped[datetime.date] = mapped_column(default=datetime.date.today)

    title: Mapped[str]
    text: Mapped[str] = mapped_column(Text, default="")

    pet_id = mapped_column(ForeignKey("pet.id"))
    pet = relationship("Pet", back_populates="article", lazy="selectin")

    def __str__(self):
        return f"{self.title}"


class ArticleAdmin(ModelView, model=Article):
    edit_template = "custom_edit.html"

    name = "статья для блога питомца"
    name_plural = "статьи для блога питомца"
    icon = "fa-solid fa-comment"
    category = "база данных питомцев"

    column_list = [
        Article.id,
        Article.date,
        Article.title,
        Article.text,
        Article.pet_id
    ]
