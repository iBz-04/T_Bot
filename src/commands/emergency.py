from telegram import Update
from telegram.ext import CallbackContext

EMERGENCY_NUMBERS = [
    ("🔥 Yangın", "110"),
    ("🚑 Ambulans", "112"),
    ("👮 Polis", "155"),
    ("🚨 AFAD (Afet ve Acil Durum)", "122"),
    ("🌲 Orman Yangını", "177"),
    ("🚤 Sahil Güvenlik", "158")
]


def acil(update: Update, context: CallbackContext):
    """Provide Istanbul emergency numbers."""
    lines = [f"{name}: {num}" for name, num in EMERGENCY_NUMBERS]
    update.message.reply_text("📞 İstanbul Acil Numaralar:\n" + "\n".join(lines))
