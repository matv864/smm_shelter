from uuid import UUID, uuid4

from sqladmin import ModelView

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

from ..base import Base

storage = FileSystemStorage(path="/storage/transaction/cheque")


class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    goal_id: Mapped[str] = mapped_column(ForeignKey("transactionGoal.id"))
    goal = relationship("TransactionGoal", lazy="selectin")

    amount: Mapped[float]
    sender_receiver: Mapped[str] = mapped_column(default="")
    comment: Mapped[str] = mapped_column(Text, default="")
    cheque: Mapped[str] = mapped_column(
        FileType(storage=storage),
        nullable=True
    )

    def __str__(self):
        return f"{self.comment}"


class TransactionAdmin(ModelView, model=Transaction):
    edit_template = "custom_edit.html"

    name = "транзакция"
    name_plural = "транзакции"
    icon = "fa-solid fa-money-bill-transfer"
    category = "отчёт"

    column_list = [
        Transaction.id,
        Transaction.goal,
        Transaction.amount,
        Transaction.sender_receiver,
        Transaction.comment,
        Transaction.cheque
    ]
