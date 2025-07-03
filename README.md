# 🤖 HOT SHARK Telegram Trading Bot

بوت تداول ذكي على تيليجرام لتحليل السوق وإرسال توصيات.

## 🚀 التشغيل

1. انسخ `.env.example` إلى `.env` وأدخل التوكن:
2. ثبّت المتطلبات:
   ```
   pip install -r requirements.txt
   ```
3. شغّل البوت:
   ```
   python main.py
   ```

أو باستخدام Docker:

```
docker build -t hot-shark-bot .
docker run -it --env-file .env hot-shark-bot
