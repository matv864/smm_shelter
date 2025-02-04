import string
import random
import logging

from bcrypt import hashpw, gensalt

from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.settings import settings

random_password = ''.join(random.SystemRandom().choice(
    string.ascii_letters + string.digits) for _ in range(
        random.randint(1, 100)
    )
) # make random string and make hash from this string
random_hash = hashpw(random_password.encode(), gensalt()).decode()


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        if not (
            settings.ADMIN_USERNAME == username and
            password == settings.ADMIN_PASSWORD
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
            logging.warning("user tried to authenticate with incorrect token")
            return False

        return True


authentication_backend = AdminAuth(secret_key=random_hash)
