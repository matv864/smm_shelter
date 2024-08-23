import os
import logging

from .models import Base
from .engine import engine


def unzip_storage():
    bash_command = 'unzip -o "/backup/storage.zip" -d /'
    os.system(f'/bin/bash -c "{bash_command}"')

    logging.info("storage is unpacked")


def create_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    logging.info("clear database is created")
