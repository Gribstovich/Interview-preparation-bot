from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.config.locales import get_help_message_content
from bot.keyboards import create_admin_edit_kb
from bot.states.admin_states import Edit


async def edit_tasks_button(message: Message, state: FSMContext) -> None:
    text = await get_help_message_content('select action')
    markup = await create_admin_edit_kb()
    await message.answer(text, reply_markup=markup)
    await state.set_state(Edit.waiting_for_action.state)
