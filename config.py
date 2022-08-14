## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABciBxsFvXlniabtNEYYE-WM27eJCto9Ena8wjR-Kkjeq7hUuChsEZ9_ijFmqJzBXulr-gix4Ffuzy8eFB7rG8BwIqQjvtBhRliAhVSwlD4EnaAk-XpHdu7OgaVHmOvcEv-oE37Iy0Z6W_UoJziZou5RLy4HQU4lmw1u23EFtvxwqvMBqTfiRCOa_tEcrUVQ4MaydBxwtf-vHW8xo0HP5LDxMdx60g0qlpsMOpXco0qrEDQzGlhid7hiDdjkcLkZiAFFKXs7HDE_pU1dQfvr1HtuupTHmha7zaDZnAi1guRK0mVy2fhnEzFPGOKIiBgsXjgDPZ0dj0ACMk7krrxpd0RAAAAAULAmq4A") 
BOT_NAME = getenv("BOT_NAME", "ayoub music")
API_ID = int(getenv("API_ID", "11054695")
API_HASH = getenv("API_HASH", "d0318694d01d4924775d3cae05aae3f7")
OWNER_NAME = getenv("OWNER_NAME", "AYOUB")
OWNER_USERNAME = getenv("OWNER_USERNAME", "xxELKANASxx")
ALIVE_NAME = getenv("ALIVE_NAME", "AYOUB")
BOT_USERNAME = getenv("BOT_USERNAME", "XxAYOUBxX_m_bot")
OWNER_ID = getenv("OWNER_ID", "5414886062")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "escobar334")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rawa2ann")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "el2hwaaa")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5414886062").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
