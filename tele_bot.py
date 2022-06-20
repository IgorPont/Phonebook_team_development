from csv import reader
from lib2to3.pgen2 import token
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
# import datetime
import user_interface

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

path = "token_bot.txt"
data = open(path, "r")
for line in data:
    token = line
data.close()

# def time_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}')

updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

# updater.dispatcher.add_handler(CommandHandler('time', time_command))




print('server start')
updater.start_polling()
updater.idle()