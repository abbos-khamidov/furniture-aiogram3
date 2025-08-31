import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database import init_db, add_user, get_user
from states import RegisterState, LoginState, ShopState
from keyboards import main_menu, colors_kb, sizes_kb, designs_kb, confirm_kb

TOKEN = ''
bot = Bot(token=TOKEN)
dp = Dispatcher()

init_db()

sessions = {}

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('добро пожаловать в магазин медели.\nВыберите действие:\n\nРегистрация: /register\nВход: /login')
    
@dp.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await message.answer('Введите ваше имя: ')
    await state.set_state(RegisterState.username)


@dp.message(RegisterState.username)
async def get_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer('Введите ваш пароль: ')
    await state.set_state(RegisterState.password)

@dp.message(RegisterState.password)
async def get_password(message: Message, state: FSMContext):
    data = await state.get_data()
    add_user(message.from_user.id, data['username'], message.text)
    await message.answer('Регистрация прошла успешно!')
    await state.clear()

# login



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
