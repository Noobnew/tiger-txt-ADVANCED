import os

API_ID = API_ID = 26702812

API_HASH = os.environ.get("API_HASH", "67af78a19eac1570697ccc64e670bd11")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6887284756:AAE-g2qKwDkuRBqz_G3qnxvRcDO8KV3o-JY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6900199673))

LOG = -1002023671255

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6900199673").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


