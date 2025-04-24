from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🚨 Acil durum! Toplanma alanı bulmak için:\n"
        "• /bul mahalle_adı yazın\n"
        "• 📍 Konumunuzu paylaşın\n"
        "• Enlem ve boylam yazın (örn: 41.2027 29.0655)\n\n"
        "🏙️ Şu an sadece Tuzla Belediyesi sınırlarında çalışır.\n"
        "Lütfen hızlı olun! ⚠️"
    )
