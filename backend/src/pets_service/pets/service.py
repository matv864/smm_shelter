from src.database.models import Pets
from src.database.my_crud import My_crud

pets_crud = My_crud(Pets, [Pets.images])


class Pets_service:
    async def get_all_pets(self):
        return await pets_crud.get(multi=True)
