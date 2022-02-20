import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PWD')
DB_NAME = os.getenv('DB_NAME')

TOKEN = os.getenv('TOKEN')
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL'))
CHANNEL = int(os.getenv('CHANNEL'))