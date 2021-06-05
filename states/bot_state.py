from aiogram.dispatcher.filters.state import StatesGroup, State


class FSM(StatesGroup):
    menu_state = State()
    add_info0 = State()
    add_info = State()
    add_info1 = State()
    add_info11 = State()
    add_info12 = State()
    add_info2 = State()
    add_info3 = State()
    add_info4 = State()
    next_day = State()
    prosmotr = State()
    izmenit_day = State()
    izmenit_day1 = State()
    izmenit_day2 = State()
    izmenit_day3 = State()
    izmenit_day4 = State()
    izmenit_day5 = State()
    changes_in_info = State()

