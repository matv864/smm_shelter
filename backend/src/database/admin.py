from fastapi import FastAPI
from sqladmin import Admin

from .engine import engine
from .security import authentication_backend
from .models import (
    PetAdmin,
    ImageAdmin,
    PetTypeAdmin,
    StatusAdmin,
    GenderAdmin
)
from .custom_views import CompressView, BackupView


def make_admin(app: FastAPI):
    admin = Admin(
        app,
        engine,
        templates_dir="src/templates",
        authentication_backend=authentication_backend
    )

    # database tables
    admin.add_view(PetAdmin)
    admin.add_view(ImageAdmin)
    admin.add_view(PetTypeAdmin)
    admin.add_view(StatusAdmin)
    admin.add_view(GenderAdmin)

    # custom views
    admin.add_view(CompressView)
    admin.add_view(BackupView)
