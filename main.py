import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Merhaba Yılmaz! Bot çalışıyor. /hizmet yaz bakalım.')

async def hizmet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hizmetler:\n1. Instagram 100 takipçi - 5 TL\n2. YouTube 1000 view - 10 TL\nSipariş için /siparis yaz.')

token = os.getenv('BOT_TOKEN')
if not token:
    print("BOT_TOKEN yok!")
    exit(1)

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hizmet", hizmet))

app.run_polling()
