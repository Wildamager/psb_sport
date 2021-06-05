from aiogram import executor, Dispatcher

from loader import dp

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # scheduler.start()
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def send_message_to_admin(dp: Dispatcher):
    # await dp.bot.send_message(config.ADMINS, "Сообщение отпралено")
    pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
