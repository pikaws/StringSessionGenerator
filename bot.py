import os

from heroku3 import from_key
from pyrogram import Client
from pyromod import listen

API_ID = int(os.environ.get("API_ID", 18049084))
API_HASH = os.environ.get("API_HASH", "7e74b1e22026fcc291d32b3d431aa21e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6307400433:AAGn1blB30MlLKpk1cI1xL6tUOPZ-cYEAp4")
APP_NAME = os.environ.get("APP_NAME", "StringSessionBot")
API_KEY = os.environ.get("API_KEY", "rnd_ZP8b5Peo73AU0azyjHjdQw68hPu2")
HU_APP = from_key(API_KEY).apps()[APP_NAME]

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
