import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database import init_db, add_user, get_user
from states import RegisterState, LoginState, ShopState
from keyboards import main_menu, colors_kb, sizes_kb, designs_kb, confirm_kb

TOKEN = '8339182289:AAGElT5QMrzAFPEBblhKcDf66pBNTDFzBtM'
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
@dp.message(Command('login'))
async def login_start(message: Message, state: FSMContext):
    await message.answer('Введите логин: ')
    await state.set_state(LoginState.username)

@dp.message(LoginState.username)
async def login_user(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer('Введите пароль: ')
    await state.set_state(LoginState.password)

@dp.message(LoginState.password)
async def get_password(message: Message, state: FSMContext):
    user = get_user(message.from_user.id)
    data = await state.get_data()
    if user and user[2] == data['username'] and user[3] == message.text:
        sessions[message.from_user.id] = user[0]
        await message.answer('Вход выполнен успешно!', reply_markup=main_menu)
    else:
        await message.answer('Неверный логин или пароль')
    await state.clear()
    
# shop
@dp.message(Command('shop'))
async def shop_start(message: Message, state: FSMContext):
    if message.from_user.id not in sessions:
        return await message.answer('Сначала войдите: /login')
    await message.answer('Выберите дизайн мебели: ', reply_markup=designs_kb)
    await state.set_state(ShopState.design)




@dp.callback_query(ShopState.design)
async def choose_design(callback: CallbackQuery, state: FSMContext):
    design = callback.data.split(':')[1]
    await state.update_data(design=design)
    await callback.message.edit_text(f'Вы выбрали дизайн: {design}\nВыберите цвет: ', reply_markup=colors_kb)
    await state.set_state(ShopState.color)





@dp.callback_query(ShopState.color)
async def choose_color(callback: CallbackQuery, state: FSMContext):
    color = callback.data.split(':')[1]
    await state.update_data(color=color)
    await callback.message.edit_text(f'Вы выбрали цвет: {color}\nВыберите размер: ', reply_markup=sizes_kb)
    await state.set_state(ShopState.size)




@dp.callback_query(ShopState.size)
async def choose_size(callback: CallbackQuery, state: FSMContext):
    size = callback.data.split(':')[1]
    await state.updata_data(size=size)
    await callback.message.edit_text(f'Вы выбрали размер: {size}\nПодтвердите покупку: 500$', reply_markup=confirm_kb)
    await state.set_state(ShopState.confirm)


@dp.callback_query(ShopState.confirm)
async def confirm_order(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'confirm_yes':
        data = await state.get_data()
        user_id = sessions[callback.from_user.id]
        add_to_cart(user_id, 'Стол', data['color'], data['size'], data['design'], 500)
        await callback.message.edit_text('Товар добавлен в корзину', reply_markup=main_menu)
    else:
        await callback.message.edit_text('Покупка отменена', reply_markup=main_menu)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
