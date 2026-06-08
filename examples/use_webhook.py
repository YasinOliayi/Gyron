from Gyron.bot import BotClient
from Gyron.filters import filters
from Gyron.models import Update

import asyncio
import requests

token = 'TOKEN'

response = requests.post(f'https://tapi.bale.ai/bot{token}/setWebhook', data= {"url" : "your_https_url/webhk"})
print(response)

app = BotClient(token, use_webhook=True)

@app.on_update(filters.equals('/start'))
async def start(update:Update):

    await app.reply('سلام')

asyncio.run(app.run(webhook_path= '/webhk'))