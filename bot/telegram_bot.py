from telegram.ext import ApplicationBuilder
from bot.handlers import setup_handlers
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    setup_handlers(app)
    print("🤖 Bot is running...")
    await app.run_polling()
