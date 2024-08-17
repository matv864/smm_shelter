from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqladmin import ModelView

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

from .base import Base


storage = FileSystemStorage(path="/storage")


class Image(Base):
    __tablename__ = "image"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid4
    )
    filename: Mapped[str] = mapped_column(FileType(storage=storage))

    pet_id = mapped_column(ForeignKey("pet.id"))
    pet = relationship("Pet", back_populates="image", lazy="selectin")

    def __str__(self):
        return f"{self.id}"


class ImageAdmin(ModelView, model=Image):
    name = "image"
    name_plural = "images"
    icon = "fa-solid fa-image"

    column_list = [
        Image.id,
        Image.filename,
        Image.pet_id
    ]

    # # search by input name
    #
    # form_ajax_refs = {
    #     "pet": {
    #         "fields": ("name",)
    #     }
    # }
