from Gyron.bot import BotClient
from Gyron.models import Update, labeled_price
from Gyron.filters import filters
import asyncio

app = BotClient('TOKEN')


@app.on_update(filters.equals('/payment'))
async def payment(update:Update):
    await app.send_invoice(update.chat.id, 'title', 'description', 'payload',
                            provider_token='PROVIDER_TOKEN', prices=[labeled_price('لیبل 1', 10000), labeled_price('لیبل 2', 10000)])
    
@app.on_update(filters.pre_checkout_query())
async def pre_checkout_query(update: Update):

    await app.answer_pre_checkout(update.pre_checkout_query.id, ok= True)

@app.on_update(filters.successful_payment())
async def succesful_payment(update: Update):

    await app.reply(f'پرداخت شما موفق بود\nمقدار واریزی : {update.successful_payment.total_amount}')
    
asyncio.run(app.run())