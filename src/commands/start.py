from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🇹🇷 Türkçe:\n\n"
        "🚨 Acil durum! Kullanılabilir komutlar:\n"
        "• /bul mahalle adı veya enlem, boylam ile en yakın toplanma alanını bulun\n"
        "• /acil ile İstanbul acil durum numaralarını görüntüleyin\n"
        "• /onlem ile deprem önlemlerini alın\n\n"
        "🏙️ Şu an sadece Tuzla Belediyesi sınırlarında çalışır.\n"
        "Lütfen hızlı olun! ⚠️\n\n"
        "🇬🇧 English:\n\n"
        "🚨 Emergency commands available:\n"
        "• /bul find nearest gathering spot by neighborhood name or latitude, longitude\n"
        "• /acil show Istanbul emergency numbers\n"
        "• /onlem show earthquake safety tips\n\n"
        "🏙️ Works only within Tuzla Municipality.\n"
        "Stay safe and act fast! ⚠️"
    )
