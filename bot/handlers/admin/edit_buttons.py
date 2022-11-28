from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.config.locales import get_help_message_content
from bot.keyboards import create_admin_edit_kb


async def admin_edit_tasks_button(message: Message, state: FSMContext) -> None:
    text = await get_help_message_content('select action')
    markup = await create_admin_edit_kb()
    await message.answer(text, reply_markup=markup)
    # something with state
