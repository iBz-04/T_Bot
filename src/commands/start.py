from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hoş geldiniz! En yakın toplanma alanını bulmak için /find_nearest <enlem> <boylam> komutunu kullanın veya konumunuzu paylaşın."
    )
