from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [123456789]  # Ganti dengan ID Telegram kamu

# Email untuk appeal WA
EMAIL_SENDER = "your.email@gmail.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Limit
FREE_LIMIT = 1
VVIP_LIMIT = 150
VVIP_DURATION_HOURS = 30
COOLDOWN_MINUTES = 1
