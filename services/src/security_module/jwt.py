import jwt
from datetime import datetime, timedelta

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
EXPIRATION_TIME_ACCESS = timedelta(minutes=30)
EXPIRATION_TIME_REFRESH = timedelta(days=3)


async def create_jwt_token(mail: str, expiration_time):
    data = {
        "mail": mail
    }
    # expiration = datetime.utcnow() + EXPIRATION_TIME
    expiration = datetime.now() + expiration_time
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


async def create_access_jwt_token(mail: str):
    return await create_jwt_token(mail, EXPIRATION_TIME_ACCESS)


async def create_refresh_jwt_token(mail: str):
    return await create_jwt_token(mail, EXPIRATION_TIME_REFRESH)


async def create_pair_tokens(mail: str):
    pair = {
        "access_token": await create_access_jwt_token(mail),
        "refresh_token": await create_refresh_jwt_token(mail)
    }
    return pair


async def verify_jwt_token(token: str):
    try:
        decoded_data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return decoded_data["mail"]
    except jwt.PyJWTError:
        return None
