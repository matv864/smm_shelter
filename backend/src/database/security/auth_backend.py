import os
import string
import random
import logging

from passlib.context import CryptContext


from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
random_hash = pwd_context.hash(''.join(random.SystemRandom().choice(
    string.ascii_letters + string.digits) for _ in range(
        random.randint(1, 100)
    )
))  # make random string and make hash from this string


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        if not (
            os.getenv("ADMIN_USERNAME") == username and
            pwd_context.verify(password, os.getenv("HASHED_PASSWORD"))
        ):
            logging.warning(
                "user entered incorrect data\n" +
                "his login: %s\n his password: %s\n",
                username,
                password
            )
            return False

        request.session.update({"token": random_hash})
        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not (token == random_hash):
            logging.warning(
                "user tried to authenticate with incorrect token\n" +
                "his referer: %s\n"
            )
            return False

        return True


authentication_backend = AdminAuth(secret_key=random_hash)
