from aiogram.types import ReplyKeyboardMarkup

from .create_universal_keyboard import create_universal_kb


async def create_admin_main_kb() -> ReplyKeyboardMarkup:
    markup = await create_universal_kb(button_names=['edit tasks', 'newsletter',
                                                     'user mode', 'help'],
                                       row_width=2)
    return markup


async def create_admin_edit_kb() -> ReplyKeyboardMarkup:
    markup = await create_universal_kb(button_names=['create category', 'del category',
                                                     'create task', 'del task',
                                                     'step back'],
                                       row_width=2)
    return markup
