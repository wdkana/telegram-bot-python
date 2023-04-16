import os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

bot = telegram.Bot(token=bot_token)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Halo! Selamat datang di bot Telegram saya.")


def puisi(update, context):
    text_puisi = "bercahayalah jiga kamu ingin dicintai setiap lawan jenis. 😉"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_puisi)


def pantun(update, context):
    text_pantun = "jalan-jalan ke jakarta barat, pulangnya beli sempolan. kalau kamu tidak ingin bersahabat, mari kita pacaran"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text_pantun)


def echo(update, context):
    message = update.message.text
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message)
    print(f"pesan dari user: {message}")


updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('puisi', puisi))
dispatcher.add_handler(CommandHandler('pantun', pantun))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()

updater.idle()
