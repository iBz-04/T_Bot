from telegram import Update
from telegram.ext import CallbackContext

PRECAUTIONS = [
    "🔒 Dolap kapaklarını kapatın, sabitleyin.",
    "🚪 Güvenli bir geçiş yolu sağlayın, çıkışları engellemeyin.",
    "🧑‍🤝‍🧑 Ailenizle acil durum planı yapın, buluşma noktası belirleyin.",
    "📱 Telefonunuzu şarjda tutun, önemli numaraları kaydedin.",
    "🧯 Yangın söndürücü, ilkyardım çantası ve su bulundurun.",
    "📶 AFAD ve deprem uygulamalarını indirin, bildirimleri açık tutun.",
    "🪟 Deprem anında: düşmeyen, sabitlenmiş eşyaların yanında ÇÖK-KAPAN-TUTUN!",
    "🚪 Deprem sonrası: binayı kontrollü şekilde terk edin, toplanma alanına gidin.",
]


def onlem(update: Update, context: CallbackContext):
    """Provide earthquake precautions for Istanbul."""
    update.message.reply_text("📋 Deprem Öncesi / Anı / Sonrası Önlemler:\n" + "\n".join(PRECAUTIONS))
