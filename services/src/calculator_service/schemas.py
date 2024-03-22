from pydantic import BaseModel


class Expression(BaseModel):
    expression: str
