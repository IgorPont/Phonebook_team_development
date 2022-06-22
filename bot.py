from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bc
from crud import get_token

token = get_token()
app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", bc.hi_command))

app.add_handler(CommandHandler("help", bc.help_command))

app.add_handler(CommandHandler("main", bc.mein_menu_command))

app.add_handler(CommandHandler("1", bc.items_command))

app.add_handler(CommandHandler("5", bc.items_command))


print('server start')
app.run_polling()
