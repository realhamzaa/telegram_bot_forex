from bot.telegram_bot import start_bot

if __name__ == '__main__':
    # استدعي الدالة بدون asyncio.run
    start_bot()  # أو إذا هي دالة async: استخدم await داخل async def main()
