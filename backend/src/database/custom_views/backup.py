import os

from sqladmin import BaseView, expose

from src.settings import settings


async def clear_old_backup() -> int:
    '''
    return status
    '''
    bash_command = "rm -rf /backup/*"
    res = os.system(f'/bin/bash -c "{bash_command}"')
    return res


async def make_db_dump() -> int:
    '''
    if num >= 0:
        return size of dump in KB
    else:
        return status of program
    '''
    command_pg_dump = settings.command_pg_dump

    bash_command = (
        f'env PGPASSWORD={settings.POSTGRES_PASSWORD} ' +
        f'/bin/bash -c "{command_pg_dump}"'
    )
    print(bash_command)
    res = os.system(bash_command)

    if os.path.isfile(settings.PATH_TO_SAVE_DUMP):
        db_dump_size_kb = os.path.getsize(
            settings.PATH_TO_SAVE_DUMP
        ) // 2**10
        return db_dump_size_kb
    return -1 * res


async def make_storage_backup() -> int:
    '''
    if num >= 0:
        return size of dump in KB
    else:
        return status of program
    '''
    comand_storage_backup = \
        f"zip -r {settings.PATH_TO_SAVE_BACKUP} /storage"
    res = os.system(f'/bin/bash -c "{comand_storage_backup}"')
    if os.path.isfile(settings.PATH_TO_SAVE_BACKUP):
        storage_backup_size_kb = os.path.getsize(
            settings.PATH_TO_SAVE_BACKUP
        ) // 2**10
        return storage_backup_size_kb
    return -1 * res


class BackupView(BaseView):
    name = "бэкап"
    icon = "fa-solid fa-warehouse"

    @expose("/backup", methods=["GET"])
    async def backup(self, request):
        await clear_old_backup()
        db_dump_size_kb = await make_db_dump()
        storage_backup_size_kb = await make_storage_backup()
        return await self.templates.TemplateResponse(
            request,
            "backup.html",
            context={
                "db_dump_size_kb": db_dump_size_kb,
                "storage_backup_size_kb": storage_backup_size_kb
            },
        )
