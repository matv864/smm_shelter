import hashlib


async def get_hashing_password(password: str) -> str:
    hash = hashlib.sha256()
    hash.update(bytes(password, 'UTF-8'))
    return hash.hexdigest()


async def match_password_with_hash(
        password: str,
        hashing_password: str
) -> bool:
    received_hashing_password = await get_hashing_password(password)
    return received_hashing_password == hashing_password
