from src.database.models import Images
from src.database.my_crud import My_crud

images_crud = My_crud(Images)


class Images_service:
    async def get_all_images_of_pet(self, pets_id):
        return await images_crud.get(
            filters=[Images.parent_id == pets_id],
            multi=True
        )
