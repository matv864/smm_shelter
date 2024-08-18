import os

from sqladmin import BaseView, expose


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
    bash_command = "pg_dump -U postgres -h smm_shelter-postgres -p 5432 " + \
        "--column-inserts pets-service > /backup/dump_pets.sql"
    res = os.system(f'/bin/bash -c "{bash_command}"')
    if res == 0:
        db_dump_size_kb = os.path.getsize("/backup/dump_pets.sql") // 2**10
        return db_dump_size_kb
    return -1 * res


async def make_storage_backup() -> int:
    '''
    if num >= 0:
        return size of dump in KB
    else:
        return status of program
    '''
    bash_command = "zip -r /backup/storage.zip /storage"
    res = os.system(f'/bin/bash -c "{bash_command}"')
    if res == 0:
        storage_backup_size_kb = os.path.getsize("/backup/storage.zip") // 2**10
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
