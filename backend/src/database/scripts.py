import os
import logging


def unzip_storage():
    bash_command = 'unzip -o "/backup/storage.zip" -d /'
    os.system(f'/bin/bash -c "{bash_command}"')

    logging.info("storage is unpacked")
