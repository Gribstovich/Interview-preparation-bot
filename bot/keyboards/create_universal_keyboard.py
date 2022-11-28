from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.config.locales import get_button_name
from bot.misc.custom_exceptions import InvalidArgumentPassed


async def create_universal_kb(button_names: list[str] | tuple[str], row_width: int = 3) -> ReplyKeyboardMarkup:
    if button_names and isinstance(button_names, (list, tuple)):
        if all((isinstance(x, str) for x in button_names)):
            button_names = (await get_button_name(x) for x in button_names)
            buttons = [KeyboardButton(btn) async for btn in button_names if isinstance(btn, str)]
            markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
            markup.add(*buttons)
            return markup
        raise InvalidArgumentPassed('button_names MUST only contain string elements.')
    raise InvalidArgumentPassed('Type of button_names MUST be a list or tuple.')
