from aiogram.types import ReplyKeyboardMarkup

from .keyboard_template import create_universal_kb


async def create_admin_main_kb() -> ReplyKeyboardMarkup:
    markup = await create_universal_kb(button_names=['edit tasks', 'newsletter',
                                                     'user mode', 'help'],
                                       row_width=2)
    return markup


async def create_admin_edit_kb() -> ReplyKeyboardMarkup:
    markup = await create_universal_kb(button_names=['create category', 'delete category',
                                                     'create task', 'delete task',
                                                     'step back'],
                                       row_width=2)
    return markup


async def create_admin_manage_kb(confirm: bool = False) -> ReplyKeyboardMarkup:
    button_names = ['step back', 'confirm'] if confirm else ['step back']
    markup = await create_universal_kb(button_names=button_names)
    return markup
