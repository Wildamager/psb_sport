from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.bot_state import FSM


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/raspisanie - Просмотр расписания на указанный день",
            "/dopolnit - Добавляем расписание на день",
            "/izmenit - Внести правки в расписание",
            "/today_and_next - Смотрим расписание сегодня-затвра")
    
    await message.answer("\n".join(text))
