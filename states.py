from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    username = State()
    password = State()

class LoginState(StatesGroup):
    username = State()
    password = State()

class ShopState(StatesGroup):
    color = State()
    size = State()
    design = State()
    confirm = State()