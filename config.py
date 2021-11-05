import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Venom")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "VENOMxCRAZY")
ALIVE_NAME = getenv("ALIVE_NAME", "Venom")
BOT_USERNAME = getenv("BOT_USERNAME", "ALEXAOP_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "V3NOM_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "V3NOM_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SUPERIOR_BOTS")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/9c4f9292c39b538719241.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/9c4f9292c39b538719241.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/9c4f9292c39b538719241.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/9c4f9292c39b538719241.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/9c4f9292c39b538719241.png")
