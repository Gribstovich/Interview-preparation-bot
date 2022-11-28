from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.config.locales import get_button_name


async def create_admin_main_kb() -> ReplyKeyboardMarkup:
    button_names = (await get_button_name(x) for x in ('edit tasks', 'newsletter', 'user mode', 'help'))
    buttons = [KeyboardButton(btn) async for btn in button_names if isinstance(btn, str)]
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(*buttons)
    return markup
