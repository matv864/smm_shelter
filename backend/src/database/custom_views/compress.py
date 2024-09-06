import os
import PIL
from PIL import Image, ImageOps
from sqladmin import BaseView, expose


FOLDER_PATH = "/storage/pets/photo"
NEED_HEIGHT_OF_PHOTO_PX = 600


async def compress_big_files():
    '''
    compression photo with changing sizes
    new height is fixed (variable NEED_HEIGHT_OF_PHOTO_PX)
    new width is counted by new height and ratio from old image
    '''
    counter_compressed_files = 0

    for filename in os.listdir(path=FOLDER_PATH):

        # check to image
        extension = filename.split(".")[-1]
        if extension.lower() not in ["jpeg", "jpg", "png"]:
            continue

        full_filename = f"{FOLDER_PATH}/{filename}"

        with Image.open(full_filename) as pill_image:
            image_height = pill_image.height
            image_width = pill_image.width

            if image_height == NEED_HEIGHT_OF_PHOTO_PX:
                continue

            ratio = image_height / image_width

            new_image_width = int(NEED_HEIGHT_OF_PHOTO_PX / ratio)

            pill_image = pill_image.resize(
                (
                    new_image_width,
                    NEED_HEIGHT_OF_PHOTO_PX
                ),
                PIL.Image.NEAREST
            )
            pill_image = ImageOps.exif_transpose(pill_image)
            pill_image.save(
                full_filename,
                optimize=True,
                compression='jpeg'
            )
        counter_compressed_files += 1

    return counter_compressed_files


class CompressView(BaseView):
    name = "сжатие изображений"
    icon = "fa-solid fa-dumbbell"
    category = "база данных питомцев"

    @expose("/compress", methods=["GET"])
    async def compress_page(self, request):
        counter_compressed_files = await compress_big_files()
        return await self.templates.TemplateResponse(
            request,
            "compress.html",
            context={
                "counter_compressed_files": str(counter_compressed_files)
            },
        )
