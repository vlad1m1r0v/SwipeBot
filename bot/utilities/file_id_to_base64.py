import io
import mimetypes
import base64

from aiogram import Bot


async def file_id_to_base64(file_id: str, bot: Bot) -> str:
    file_info = await bot.get_file(file_id)

    mime_type, _ = mimetypes.guess_type(file_info.file_path)

    if not mime_type:
        mime_type = "application/octet-stream"

    file_buffer = io.BytesIO()
    await bot.download_file(file_info.file_path, destination=file_buffer)

    file_buffer.seek(0)

    base64_encoded_image = base64.b64encode(file_buffer.read()).decode('utf-8')

    return f"data:{mime_type};base64,{base64_encoded_image}"