from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("dopolnit", "Добавлять/делать правки в расписании"),
            types.BotCommand("raspisanie", "Просмотр расписания на указанный день"),
            types.BotCommand("izmenit","Внести правки в расписание"),
            types.BotCommand("today_and_next", "Смотрим расписание сегодня-затвра"),

        ]
    )
