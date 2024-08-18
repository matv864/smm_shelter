import os

from .models import Base
from .engine import engine


def unzip_storage():
    bash_command = 'unzip -o "/backup/storage.zip" -d /'
    os.system(f'/bin/bash -c "{bash_command}"')


def create_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
