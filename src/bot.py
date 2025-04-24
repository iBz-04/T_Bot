from telegram.ext import Updater, CommandHandler
from commands.start import start
from commands.find_nearest import bul
from commands.emergency import acil
from commands.precautions import onlem
from config import TELEGRAM_TOKEN

def main():
    print("Bot started")
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('bul', bul))
    dp.add_handler(CommandHandler('acil', acil))
    dp.add_handler(CommandHandler('onlem', onlem))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
