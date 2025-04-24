from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🚨 Acil durum! Kullanılabilir komutlar:\n"
        "• /bul <mahalle adı> veya <enlem> <boylam> ile en yakın toplanma alanını bulun\n"
        "• /acil ile İstanbul acil durum numaralarını görüntüleyin\n"
        "• /onlem ile deprem önlemlerini alın\n\n"
        "🏙️ Şu an sadece Tuzla Belediyesi sınırlarında çalışır.\n"
        "Lütfen hızlı olun! ⚠️"
    )
