from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqladmin import ModelView

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

from ..base import Base


storage = FileSystemStorage(path="/storage/pets/photo")


class PetImage(Base):
    __tablename__ = "petImage"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    filename: Mapped[str] = mapped_column(FileType(storage=storage))

    pet_id = mapped_column(ForeignKey("pet.id"))
    pet = relationship("Pet", back_populates="petImage", lazy="selectin")

    def __str__(self):
        return f"{self.id}"


class PetImageAdmin(ModelView, model=PetImage):
    name = "изображение"
    name_plural = "изображения"
    icon = "fa-solid fa-image"
    category = "база данных питомцев"

    column_list = [
        PetImage.id,
        PetImage.filename,
        PetImage.pet_id
    ]
