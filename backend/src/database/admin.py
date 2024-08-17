from fastapi import FastAPI
from sqladmin import Admin

from .engine import engine
from .security import authentication_backend
from .models import PetAdmin, ImageAdmin
from .custom_views import CompressView


def make_admin(app: FastAPI):
    admin = Admin(
        app,
        engine,
        templates_dir="src/templates",
        authentication_backend=authentication_backend
    )

    admin.add_view(PetAdmin)
    admin.add_view(ImageAdmin)

    admin.add_view(CompressView)
