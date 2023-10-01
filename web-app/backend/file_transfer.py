import aiohttp
from constants import TEMPORARY_IMAGE_FILE_PATH

async def download_file_from_url(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

async def dowload_image_from_form_data(data):
    img_bytes = await (data["file"].read())
    with open(TEMPORARY_IMAGE_FILE_PATH, 'wb') as f: f.write(img_bytes)