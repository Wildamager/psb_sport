# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#
# from loader import dp, bot
#
# inline_btn_1 = InlineKeyboardButton('Июнь', callback_data='button1')
# inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
# inline_btn_0 = InlineKeyboardButton(' ', callback_data='btn3')
# inline_btn_2 = InlineKeyboardButton('1', callback_data='btn3')
# inline_btn_3 = InlineKeyboardButton('2', callback_data='btn4')
# inline_btn_4 = InlineKeyboardButton('3', callback_data='btn5')
# inline_btn_5 = InlineKeyboardButton('4', callback_data='btn3')
# inline_btn_6 = InlineKeyboardButton('5', callback_data='btn4')
# inline_btn_7 = InlineKeyboardButton('6', callback_data='btn5')
# inline_btn_8 = InlineKeyboardButton('7', callback_data='btn3')
# inline_btn_9 = InlineKeyboardButton('8', callback_data='btn4')
# inline_btn_10 = InlineKeyboardButton('9', callback_data='btn5')
# inline_btn_11 = InlineKeyboardButton('10', callback_data='btn3')
# inline_btn_12 = InlineKeyboardButton('11', callback_data='btn4')
# inline_btn_13 = InlineKeyboardButton('12', callback_data='btn5')
# inline_btn_14 = InlineKeyboardButton('13', callback_data='btn3')
# inline_btn_15 = InlineKeyboardButton('14', callback_data='btn4')
# inline_btn_16 = InlineKeyboardButton('15', callback_data='btn5')
# inline_btn_17 = InlineKeyboardButton('16', callback_data='btn3')
# inline_btn_18 = InlineKeyboardButton('17', callback_data='btn4')
# inline_btn_19 = InlineKeyboardButton('18', callback_data='btn5')
# inline_btn_20 = InlineKeyboardButton('19', callback_data='btn3')
# inline_btn_21 = InlineKeyboardButton('20', callback_data='btn4')
# inline_btn_22 = InlineKeyboardButton('21', callback_data='btn5')
# inline_btn_23 = InlineKeyboardButton('22', callback_data='btn3')
# inline_btn_24 = InlineKeyboardButton('23', callback_data='btn4')
# inline_btn_25 = InlineKeyboardButton('24', callback_data='btn5')
# inline_btn_26 = InlineKeyboardButton('25', callback_data='btn3')
# inline_btn_27 = InlineKeyboardButton('26', callback_data='btn4')
# inline_btn_28 = InlineKeyboardButton('27', callback_data='btn5')
# inline_btn_29 = InlineKeyboardButton('28', callback_data='btn3')
# inline_btn_30 = InlineKeyboardButton('29', callback_data='btn4')
# inline_btn_31 = InlineKeyboardButton('30', callback_data='btn5')
# inline_kb2 = InlineKeyboardMarkup()
# inline_kb2.row(inline_btn_0, inline_btn_2, inline_btn_3, inline_btn_4,inline_btn_5, inline_btn_6, inline_btn_7).row(inline_btn_8, inline_btn_9, inline_btn_10,inline_btn_11, inline_btn_12, inline_btn_13,inline_btn_14).row( inline_btn_15, inline_btn_16,inline_btn_17, inline_btn_18, inline_btn_19,inline_btn_20, inline_btn_21).row( inline_btn_22,inline_btn_23, inline_btn_24, inline_btn_25,inline_btn_26, inline_btn_27, inline_btn_28).row(inline_btn_29, inline_btn_30, inline_btn_31,inline_btn_0,inline_btn_0,inline_btn_0,inline_btn_0)
# #
# #Эхо хендлер, куда летят текстовые сообщения без указанного состояния
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(f"Эхо без состояния."
#                          f"Сообщение:\n"
#                          f"{message.text}",reply_markup=inline_kb1)
#
# @dp.callback_query_handler()
# async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
#     code = callback_query.data[-1]
#     if code.isdigit():
#         code = int(code)
#     if code == 2:
#         await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
#     elif code == 5:
#         await bot.answer_callback_query(
#             callback_query.id,
#             text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
#     else:
#         await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}',reply_markup=inline_kb2)
#
# @dp.edited_message_handler(content_types=types.ContentTypes.LOCATION)
# async def on_geo_change(message: types.Message):
#     await message.answer(f"геоданные изменены\n"
#                          f"{message}",)
#
# # Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# # @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# # async def bot_echo_all(message: types.Message, state: FSMContext):
# #     state = await state.get_state()
# #     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
# #                          f"\nСодержание сообщения:\n"
# #                          f"<code>{message}</code>")
