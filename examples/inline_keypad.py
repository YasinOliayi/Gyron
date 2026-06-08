from Gyron.bot import BotClient
from Gyron.models import Update, InlineButton, InlineRow, InlineKeypad, copy_text_button
from Gyron.filters import filters
import asyncio

app = BotClient('TOKEN')

keypad = InlineKeypad(
    rows= [
        InlineRow(
            buttons= [
                InlineButton(text= 'دکمه 1', data= 'btn1', copy_text= copy_text_button('متنی که باید کپی بشه'))
            ]
        ),
        InlineRow(
            buttons= [
                InlineButton(text= 'دکمه 2', data='btn2')
            ]

        )
    ]
)

@app.on_update(filters.text('/start'))
async def start(update:Update):

    await app.reply(f'تست inline keypad', markup= keypad)


@app.on_update(filters.callbhack_query('btn2'))
async def button2(update:Update):

    await app.send_message(update.callback_query.message.chat.id, f'کلیک کردی روی دکمه 2')


asyncio.run(app.run())