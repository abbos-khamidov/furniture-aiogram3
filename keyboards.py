from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='/shop'), KeyboardButton(text='/cart')],
        [KeyboardButton(text='/logout')]
    ],
    resize_keyboard=True
)

colors_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Белый', callback_data='color:белый')],
    [InlineKeyboardButton(text='Черный', callback_data='color:черный')],
    [InlineKeyboardButton(text='Дерево', callback_data='color:дерево')],
])

sizes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='S', callback_data='size:s')],
    [InlineKeyboardButton(text='M', callback_data='size:m')],
    [InlineKeyboardButton(text='L', callback_data='size:l')],
])

designs_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Классика', callback_data='design:классика')],
    [InlineKeyboardButton(text='Модерн', callback_data='design:модерн')],
    [InlineKeyboardButton(text='Лофт', callback_data='design:лофт')],
])

confirm_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить в корзину', callback_data='confirm:yes'), 
    InlineKeyboardButton(text='Отменить', callback_data='confirm:no')]
])
