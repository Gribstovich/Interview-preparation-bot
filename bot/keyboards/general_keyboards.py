from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot import database as db


async def create_categories_kb(select=False) -> ReplyKeyboardMarkup:
    cartegories = await db.fetchall(table='categories', columns=['category_name'])
    button_names = [KeyboardButton(btn['category_name']) for btn in cartegories]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*button_names)
    return markup
