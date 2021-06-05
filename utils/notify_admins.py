import logging

from aiogram import Dispatcher

from data import config


async def on_startup_notify(dp: Dispatcher):

    try:
        await dp.bot.send_message(config.ADMINS, "Бот Запущен")
    except Exception as err:
        logging.exception(err)
