"""Runtime configuration, read from environment variables.

Copy `.env.dist` to `.env` and fill in the values before starting the bot.
"""
from environs import Env

env = Env()
env.read_env()

try:
    BOT_TOKEN = env.str("BOT_TOKEN")
except Exception:
    raise SystemExit(
        "BOT_TOKEN is not set. Copy .env.dist to .env and put your bot token there."
    )

ADMINS = env.list("ADMINS", default=[], cast=int)

if not ADMINS:
    raise SystemExit(
        "ADMINS is empty. Put your Telegram user id(s) into .env as a comma separated list."
    )
