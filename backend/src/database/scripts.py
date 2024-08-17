from .models import Base
from .engine import engine


def create_database():
    Base.metadata.create_all(engine)
