from Gyron.bot import BotClient
from Gyron.models import Update, input_media_photo
import asyncio
from Gyron.enums import inputmediagrouptype

app = BotClient('TOKEN')

@app.on_update()
async def sendmediagroup(update:Update):
    await app.reply(update.text)
    await app.send_media_group(
    update.chat.id,
    [
        input_media_photo(
            type=inputmediagrouptype.photo,
            media="your photo download link", is_local_file=False
        ),
        input_media_photo(
            type='photo',media="my_photo.jpg", is_local_file= True
      
        )
     
    ]
)

"""
Notes:
    - If the file is stored locally, set `is_local_file=True`
      and pass the file path in `media`.

    - When uploading files using multipart/form-data, each file
      must have a unique name. Two files with the same filename
      cannot be uploaded in the same media group.

    - A media group must contain at least two media items.
      To send a single file, use the corresponding send method
      (e.g. sendPhoto, sendVideo, sendDocument, ...).
"""

asyncio.run(app.run())