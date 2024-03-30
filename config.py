import os

API_ID = API_ID = 25919081

API_HASH = os.environ.get("API_HASH", "0bc2fdba14b16b44f0d89729ed8d2118")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6846325385:AAGF5EQTa54YpQdBe21op8RCwi6WJMz96JQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1826828317))

LOG = -1002015954185,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


