# psb_sport

Telegram bot for a sports school: a starting point for the bot that shows the
schedule, keeps student records in a database and sends announcements to the
groups. Written with **aiogram 2** and **SQLAlchemy**.

**Status: work in progress.** The repository is a skeleton from 2021, kept as a
reference for the structure of an aiogram bot with a database layer. What is
actually usable today:

- bot startup with configuration from the environment (`data/config.py`);
- FSM state machine for the schedule and student records (`states/bot_state.py`);
- reply and inline keyboards (`keyboards/`);
- SQLAlchemy helpers for reading and writing the schedule (`utils/db_api/`);
- throttling middleware (`middlewares/throttling.py`).

What is **not** finished: the `groups` and `channels` handler packages are empty,
the admin filter is commented out in `filters/__init__.py`, the scheduler job in
`handlers/users/rassilka.py` is commented out, and `handlers/users/start.py`
still contains layout placeholders and a hardcoded image URL.

## Stack

| Part | Technology |
|---|---|
| Bot | aiogram 2.12, Python 3 |
| Database | SQLite via SQLAlchemy 1.3 |
| Scheduling | APScheduler 3 (job is currently disabled) |
| Configuration | environs, values from `.env` |

## Getting started

```bash
git clone https://github.com/Wildamager/psb_sport.git
cd psb_sport
python -m venv .venv
# Windows: .venv\Scripts\activate   Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt

cp .env.dist .env      # Linux/macOS: cp .env.dist .env
```

Fill in `.env`:

```ini
BOT_TOKEN=123456789:token-from-botfather
ADMINS=11111111,22222222
```

Then start long polling:

```bash
python app.py
```

The bot refuses to start without `BOT_TOKEN` and `ADMINS`, so a missing
configuration fails immediately with a readable message instead of an
`AttributeError` deep inside aiogram.

## Configuration

| Variable | Required | Meaning |
|---|---|---|
| `BOT_TOKEN` | yes | Bot token from [@BotFather](https://t.me/BotFather) |
| `ADMINS` | yes | Telegram user ids that get the startup notification, comma separated |
| `DB_NAME` | no | SQLite database name, `SPORT.db` by default |

`.env` is git-ignored. The repository used to contain SQLite files with real
user ids; they were removed and `*.db` is ignored from now on.

## Project layout

```
app.py                     entry point: long polling, startup hooks
loader.py                  Bot and Dispatcher instances
data/config.py             configuration from the environment
handlers/users/            start, help, echo, mailing
handlers/groups/           empty, planned group chats
handlers/channels/         empty, planned channels
handlers/errors/           error handler
keyboards/                 reply and inline keyboards
middlewares/throttling.py  rate limiting per handler
states/bot_state.py        FSM states
utils/db_api/              SQLAlchemy helpers for the schedule
utils/misc/                logging and throttling helpers
```

## Tests

There are no automated tests. `utils/db_api/test.py` and `db_test.py` are
manual scripts left from development.

## License

MIT, see [LICENSE](LICENSE).
