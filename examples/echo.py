from Gyron.bot import BotClient
from Gyron.models import Update
import asyncio

app = BotClient('TOKEN')

@app.on_update()
async def echo(update:Update):
    await app.reply(update.text)

asyncio.run(app.run())