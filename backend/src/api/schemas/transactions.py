from pydantic import BaseModel


class Transaction_schema(BaseModel):
    goal: "TransactionGoal_schema"
    amount: float
    sender_receiver: str
    comment: str
    cheque: str


class TransactionGoal_schema(BaseModel):
    goal: str
