import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CSV_PATH = os.getenv('CSV_PATH', 'toplanma.csv')

if not TELEGRAM_TOKEN:
    raise ValueError('TELEGRAM_TOKEN is not set in environment variables')
