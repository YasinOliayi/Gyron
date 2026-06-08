from Gyron.bot import BotClient
from Gyron.models import Update
from Gyron.filters import filters
from Gyron.state import StateManager
import asyncio

app = BotClient('TOKEN')
state_system = StateManager(auto_clear=True) 

"""
auto_clear:
If enabled, the state will be automatically removed from memory after it expires.

expire:
Sets the state expiration time.

"""

@app.on_update(filters.text('شروع'))
async def set_state(message:Update):

    await state_system.set_state_for(message, 'awaiting_email', expire= 100)
    await app.reply('لطفا ایمیل خود را ارسال کنید')

@app.on_update(filters.text('کنسل'))
async def clear_state(message:Update):

    await state_system.clear_state_for(message)
    await app.reply('کنسل شد')

@app.on_update(filters.at_state(state_system, 'awaiting_email'))
async def state(message:Update):

    await app.reply(f'دریافت شد : {message.text}')
 

asyncio.run(app.run())