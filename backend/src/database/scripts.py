from .models import Base
from .engine import engine


def create_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
