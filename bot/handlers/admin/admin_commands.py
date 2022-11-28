from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.config.locales import get_help_message_content
from bot.keyboards import create_admin_main_kb


async def admin_start_command(message: Message, state: FSMContext) -> None:
    text = await get_help_message_content('admin mode')
    markup = await create_admin_main_kb()
    await message.answer(text, reply_markup=markup)
    await state.finish()
