from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqladmin import ModelView

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

from ..base import Base


storage = FileSystemStorage(path="/storage/news/photo")


class NewsImage(Base):
    __tablename__ = "newsImage"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    filename: Mapped[str] = mapped_column(FileType(storage=storage))

    news_id = mapped_column(ForeignKey("news.id"))
    news = relationship("News", back_populates="newsImage", lazy="selectin")

    def __str__(self):
        return f"{self.id}"


class NewsImageAdmin(ModelView, model=NewsImage):
    name = "фотка для новости"
    name_plural = "фотки для новостей"
    icon = "fa-solid fa-camera"
    category = "новости"

    column_list = [
        NewsImage.id,
        NewsImage.filename,
        NewsImage.news_id
    ]
