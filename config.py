import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27079591")) #optional
API_HASH = getenv("API_HASH", "c81ae4c3dc026ea4bf49842a8ce4a5f9") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7403621976").split()))
OWNER_ID = 7009601543
MONGO_URL = "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"
BOT_TOKEN = "7656510911:AAHx2GcEV9q_HOQ5NjysO1V2cMdAaVQpz8Y"
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/5badd2112e1e0cdf03a1f.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = -1002356967761
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/badmunda011/test")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
