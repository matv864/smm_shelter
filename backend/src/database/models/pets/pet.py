from uuid import UUID, uuid4
from datetime import date

from sqladmin import ModelView

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text

from ..base import Base


class Pet(Base):
    __tablename__ = "pet"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    status_id: Mapped[str] = mapped_column(ForeignKey("status.id"))
    status = relationship("Status", lazy="selectin")

    name: Mapped[str]

    gender_id: Mapped[str] = mapped_column(ForeignKey("gender.id"))
    gender = relationship("Gender", lazy="selectin")

    type_id: Mapped[str] = mapped_column(ForeignKey("petType.id"))
    type = relationship("PetType", lazy="selectin")

    year_birth: Mapped[date] = mapped_column(
        nullable=True,
        default=date.today
    )
    in_shelter_from: Mapped[date] = mapped_column(
        nullable=True,
        default=date.today
    )

    description: Mapped[str] = mapped_column(Text, default="")

    petImage = relationship(
        "PetImage",
        back_populates="pet",
        lazy="selectin"
    )

    article = relationship(
        "Article",
        back_populates="pet",
        lazy="selectin"
    )

    def __str__(self):
        return f"{self.name}"


class PetAdmin(ModelView, model=Pet):
    edit_template = "custom_edit.html"

    name = "питомец"
    name_plural = "питомцы"
    icon = "fa-solid fa-paw"
    category = "база данных питомцев"

    column_list = [
        Pet.status,
        Pet.name,
        Pet.gender,
        Pet.type,
        Pet.description
    ]
    form_excluded_columns = [
        Pet.petImage,
        Pet.article
    ]
    column_searchable_list = [Pet.name]
