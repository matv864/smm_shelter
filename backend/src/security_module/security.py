from fastapi import HTTPException

from .secret_schema import Secret_schema


async def verify_user(payload: Secret_schema) -> bool:
    if len(payload.password) < 3:
        raise HTTPException(status_code=403, detail="wrong password")
