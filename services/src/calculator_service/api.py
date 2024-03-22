from fastapi import APIRouter

from src.calculator_service.calculate import calculate_this
from src.calculator_service.schemas import Expression

calc_router = APIRouter()


@calc_router.post("/calculate")
async def calculate(expression: Expression):
    return await calculate_this(expression.expression)
