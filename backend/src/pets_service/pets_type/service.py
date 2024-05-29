from src.database.models import Pets_type
from src.database.my_crud import My_crud

pets_type_crud = My_crud(Pets_type)


class Pets_type_service:
    async def get_all_pets_type(self):
        return await pets_type_crud.get(multi=True)
