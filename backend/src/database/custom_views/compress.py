import os
import PIL
from PIL import Image
from sqladmin import BaseView, expose

MAX_FILE_SIZE_KB = 2**10


async def compress_big_files():
    counter_compressed_files = 0
    for filename in os.listdir(path='/storage'):
        full_filename = f"/storage/{filename}"

        file_size_kb = os.path.getsize(full_filename) // 2**10
        # // 2**10 is from B to KB

        if file_size_kb <= MAX_FILE_SIZE_KB:
            continue
        if file_size_kb < 3*2**10:
            need_quality = 50
        else:
            need_quality = 30

        with Image.open(full_filename) as pill_image:
            pill_image = pill_image.resize(
                (pill_image.width, pill_image.height),
                PIL.Image.NEAREST
            )
            pill_image.save(
                full_filename,
                optimize=True,
                quality=need_quality
            )
        counter_compressed_files += 1

    return counter_compressed_files


class CompressView(BaseView):
    name = "Compress Images"
    icon = "fa-solid fa-dumbbell"

    @expose("/compress", methods=["GET"])
    async def compress_page(self, request):
        counter_compressed_files = await compress_big_files()
        return await self.templates.TemplateResponse(
            request,
            "message.html",
            context={
                "view_name": self.name,
                "message": f"{counter_compressed_files} files is compessed"
            },
        )
