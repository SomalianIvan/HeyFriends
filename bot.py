from telegram.ext import InlineQueryHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='646524007:AAHMlqmKmGg-00Im4b8WuzI-AaxlvtLvF6o', use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(update, context):
    """Echo the user message."""
    if "Hey friends," in update.message.text:
        update.message.reply_text("What a great idea. How about today?")
    if "boardgames" in update.message.text or " bg " in update.message.text:
        update.message.reply_text("Boardgames are for nerds.")

dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
