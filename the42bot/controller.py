import re

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from the42bot.logger import Bot42Logger
from the42bot.model import InputBot

thelogger = Bot42Logger.getLogger('./the42bot.log')


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(f"Hi {user['first_name']}!")


def help(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(f"I am not your slave, {user['first_name']}!")


def echo(update: Update, context: CallbackContext):
    text = update.message.text
    text = re.sub("[aeou]", "i", text)
    text = re.sub("[áéóú]", "í", text)
    text = re.sub("[AEOU]", "I", text)
    text = re.sub("[ÁÉÓÚ]", "Í", text)
    update.message.reply_text(text)


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    thelogger.warning('Update "%s" caused error "%s"', update, context.error)


class BotController:

    def __init__(self, input_bot: InputBot):
        self.token = input_bot.token

    def execute(self):
        updater = Updater(token=self.token, use_context=True)
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()
