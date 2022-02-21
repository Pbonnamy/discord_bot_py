import os

import discord
import mysql
from dotenv import load_dotenv

load_dotenv()

DB = None
DB_CURSOR = None

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PWD')
DB_NAME = os.getenv('DB_NAME')

TOKEN = os.getenv('TOKEN')
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL'))
FEED_CHANNEL = int(os.getenv('FEED_CHANNEL'))
CHANNEL = int(os.getenv('CHANNEL'))


def connect_db():
    global DB
    global DB_CURSOR

    DB = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    DB_CURSOR = DB.cursor()
