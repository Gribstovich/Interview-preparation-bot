from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.config.locales import get_help_message_content
from bot.keyboards import create_admin_main_kb


async def start_admin_command(message: Message, state: FSMContext) -> None:
    text = await get_help_message_content('start_admin')
    markup = await create_admin_main_kb()
    await message.answer(text, reply_markup=markup)
    await state.finish()
