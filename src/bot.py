from telegram.ext import Updater, CommandHandler
from commands.start import start
from commands.find_nearest import find_nearest
from config import TELEGRAM_TOKEN

def main():
    print("Bot started")
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('find_nearest', find_nearest))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
