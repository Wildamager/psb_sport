from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, ReplyKeyboardMarkup, \
    KeyboardButton

from keyboards.default.but import where_place_murkup, check_place
from loader import dp, bot
from states.bot_state import FSM


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await bot.send_photo(message.chat.id, 'https://im0-tub-ru.yandex.net/i?id=3218ff2f5f84ec6c027a065b6c24399b-l&n=13')
    await message.answer(f"Привет {message.from_user.full_name}, добро пожаловать в бота ПСБ Спорт!"
                         f"\nВыберете регион, в котором находитесь, чтобы получить информацию о меропиятиях"
                         f"в рамках проекта ПСБ Спорт.", reply_markup=where_place_murkup)

    await FSM.menu_state.set()


inline_btn_1 = InlineKeyboardButton('Июнь', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


@dp.message_handler(state=FSM.menu_state)
async def bot_help(message: types.Message):
    if message.text == 'Назад':
        await bot.send_photo(message.chat.id,
                             'https://im0-tub-ru.yandex.net/i?id=3218ff2f5f84ec6c027a065b6c24399b-l&n=13', )
        await message.answer(f"Привет {message.from_user.full_name}, добро пожаловать в бота ПСБ Спорт!"
                             f"\nВыберете регион, в котором находитесь, чтобы получить информацию о меропиятиях"
                             f"в рамках проекта ПСБ Спорт.", reply_markup=where_place_murkup)
    else:
        if message.text in check_place:
            await message.answer(f"Вы выбрали {message.text}", reply_markup=ReplyKeyboardRemove())
            await message.answer(f"Выберете месяц проведения мероприятия.", reply_markup=inline_kb1)
            # await FSM.test_state1.set()
        else:
            await message.answer('Не понимаю')


inline_btn_0 = InlineKeyboardButton(' ', callback_data='btn3')
inline_btn_2 = InlineKeyboardButton('1', callback_data='btn3')
inline_btn_3 = InlineKeyboardButton('2', callback_data='btn4')
inline_btn_4 = InlineKeyboardButton('3', callback_data='btn5')
inline_btn_5 = InlineKeyboardButton('4', callback_data='btn3')
inline_btn_6 = InlineKeyboardButton('5', callback_data='test')
inline_btn_7 = InlineKeyboardButton('6', callback_data='btn5')
inline_btn_8 = InlineKeyboardButton('7', callback_data='btn3')
inline_btn_9 = InlineKeyboardButton('8', callback_data='btn4')
inline_btn_10 = InlineKeyboardButton('9', callback_data='btn5')
inline_btn_11 = InlineKeyboardButton('10', callback_data='btn3')
inline_btn_12 = InlineKeyboardButton('11', callback_data='btn4')
inline_btn_13 = InlineKeyboardButton('12', callback_data='btn5')
inline_btn_14 = InlineKeyboardButton('13', callback_data='btn3')
inline_btn_15 = InlineKeyboardButton('14', callback_data='btn4')
inline_btn_16 = InlineKeyboardButton('15', callback_data='btn5')
inline_btn_17 = InlineKeyboardButton('16', callback_data='btn3')
inline_btn_18 = InlineKeyboardButton('17', callback_data='btn4')
inline_btn_19 = InlineKeyboardButton('18', callback_data='btn5')
inline_btn_20 = InlineKeyboardButton('19', callback_data='btn3')
inline_btn_21 = InlineKeyboardButton('20', callback_data='btn4')
inline_btn_22 = InlineKeyboardButton('21', callback_data='btn5')
inline_btn_23 = InlineKeyboardButton('22', callback_data='btn3')
inline_btn_24 = InlineKeyboardButton('23', callback_data='btn4')
inline_btn_25 = InlineKeyboardButton('24', callback_data='btn5')
inline_btn_26 = InlineKeyboardButton('25', callback_data='btn3')
inline_btn_27 = InlineKeyboardButton('26', callback_data='btn4')
inline_btn_28 = InlineKeyboardButton('27', callback_data='btn5')
inline_btn_29 = InlineKeyboardButton('28', callback_data='btn3')
inline_btn_30 = InlineKeyboardButton('29', callback_data='btn4')
inline_btn_31 = InlineKeyboardButton('30', callback_data='btn5')
inline_kb2 = InlineKeyboardMarkup()
inline_kb2.row(inline_btn_0, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7).row(
    inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12, inline_btn_13, inline_btn_14).row(
    inline_btn_15, inline_btn_16, inline_btn_17, inline_btn_18, inline_btn_19, inline_btn_20, inline_btn_21).row(
    inline_btn_22, inline_btn_23, inline_btn_24, inline_btn_25, inline_btn_26, inline_btn_27, inline_btn_28).row(
    inline_btn_29, inline_btn_30, inline_btn_31, inline_btn_0, inline_btn_0, inline_btn_0, inline_btn_0)


@dp.callback_query_handler(state=FSM.menu_state)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Календарь событий на Июнь', reply_markup=inline_kb2)
    await FSM.add_info.set()


inline_btn = InlineKeyboardButton('Регестрация', callback_data='reg')
regestration = InlineKeyboardMarkup()
regestration.row(inline_btn)


@dp.callback_query_handler(state=FSM.add_info)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    if callback_query.data == 'test':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               f"<a href='{'https://urban.heroleague.ru/'}'>ГОНКА ГЕРОЕВ URBAN</a>",
                               reply_markup=regestration, parse_mode="HTML")
        await FSM.add_info1.set()


inline_btn1 = InlineKeyboardButton('Я участник', callback_data='uch')
inline_btn2 = InlineKeyboardButton('Я болельщик', callback_data='bol')
kem_yavl = InlineKeyboardMarkup()
kem_yavl.row(inline_btn1, inline_btn2)


@dp.callback_query_handler(state=FSM.add_info1)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    if callback_query.data == 'reg':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               f"Кем Вы являетесь на мероприятии?",
                               reply_markup=kem_yavl)
        await FSM.add_info11.set()

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)


@dp.callback_query_handler(state=FSM.add_info11)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    if callback_query.data == 'uch':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               f"Поделитесь геоданными.",
                               reply_markup=markup_request)
    elif callback_query.data == 'bol':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               f"Поделитесь геоданными.",
                               reply_markup=markup_request)

