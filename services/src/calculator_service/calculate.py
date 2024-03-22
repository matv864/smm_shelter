from math import (
    sin,
    cos,
    tan,
    asin,
    acos,
    atan,
    degrees,
    radians,
    pi,
    e,
    log,
    pow,
    sqrt,
    factorial,
    ceil,
    floor,
    trunc
)

from src.calculator_service.math_funcs import (
    cot,
    acot
)


FUNC_NAMES = [
    "",
    "sin",
    "cos",
    "tan",
    "cot",
    "asin",
    "acos",
    "atan",
    "acot",
    "degrees",
    "radians",
    "pi",
    "e",
    "log",
    "pow",
    "sqrt",
    "factorial",
    "ceil",
    "floor",
    "trunc",
    "abs"
]


async def check_name(func_name):
    return func_name in FUNC_NAMES


async def calculate_this(expression: str) -> str | None:
    expression = expression.lower()
    func_name = ""
    for sym in expression:
        if not "a" <= sym <= "z":
            if not await check_name(func_name):
                return None
            func_name = ""
        else:
            func_name += sym

    if not await check_name(func_name):
        return None

    try:
        return str(eval(expression))
    except Exception:
        return None
