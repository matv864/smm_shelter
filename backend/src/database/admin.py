from fastapi import FastAPI
from sqladmin import Admin

from .engine import engine
from .security import authentication_backend
from .models import (
    PetAdmin,
    PetImageAdmin,
    PetTypeAdmin,
    StatusAdmin,
    GenderAdmin,
    ArticleAdmin,

    NewsAdmin,
    NewsImageAdmin,

    TransactionAdmin,
    TransactionGoalAdmin,
    ReportCommentAdmin,
    ReportTypeAdmin
)
from .custom_views import CompressView, BackupView


def make_admin(app: FastAPI):
    admin = Admin(
        app,
        engine,
        title="zooprim125",
        logo_url="https://zooprim125.ru/favicon.ico",
        templates_dir="src/templates",
        authentication_backend=authentication_backend
    )

    # database tables
    admin.add_view(PetAdmin)
    admin.add_view(PetImageAdmin)
    admin.add_view(PetTypeAdmin)
    admin.add_view(StatusAdmin)
    admin.add_view(GenderAdmin)
    admin.add_view(ArticleAdmin)

    admin.add_view(NewsAdmin)
    admin.add_view(NewsImageAdmin)

    admin.add_view(TransactionAdmin)
    admin.add_view(TransactionGoalAdmin)
    admin.add_view(ReportCommentAdmin)
    admin.add_view(ReportTypeAdmin)

    # custom views
    admin.add_view(CompressView)
    admin.add_view(BackupView)
