from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا بك في HOT SHARK Bot! 🦈")

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
