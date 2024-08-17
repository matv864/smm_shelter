import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqladmin import ModelView

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

from .base import Base


storage = FileSystemStorage(path="/storage")


class Image(Base):
    __tablename__ = "image"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        unique=True,
        default=uuid.uuid4
    )
    filename: Mapped[str] = mapped_column(FileType(storage=storage))

    pet_id = mapped_column(ForeignKey("pet.id"))
    pet = relationship("Pet", back_populates="image", lazy="selectin")

    def __str__(self):
        return f"{self.id}"


class ImageAdmin(ModelView, model=Image):
    column_list = [
        Image.id,
        Image.filename,
        Image.pet_id
    ]

    form_ajax_refs = {
        "pet": {
            "fields": ("name",)
        }
    }
