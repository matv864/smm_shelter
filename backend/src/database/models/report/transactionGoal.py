from uuid import UUID, uuid4

from sqladmin import ModelView

from sqlalchemy.orm import Mapped, mapped_column

from ..base import Base


class TransactionGoal(Base):
    __tablename__ = "transactionGoal"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    goal: Mapped[str]

    def __str__(self):
        return f"{self.goal}"


class TransactionGoalAdmin(ModelView, model=TransactionGoal):
    name = "цель транзакции"
    name_plural = "цели транзакций"
    icon = "fa-solid fa-location-arrow"
    category = "отчёт"

    column_list = [
        TransactionGoal.goal
    ]

    column_searchable_list = [TransactionGoal.goal]
