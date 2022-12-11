from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot import database as db
from bot.config.locales import get_help_message_content
from bot.keyboards import create_admin_edit_kb, create_admin_manage_kb
from bot.services import category_is_exists_check
from bot.states.admin_states import EditCategories, Edit


async def create_category_button(message: Message, state: FSMContext) -> None:
    text = await get_help_message_content('send category name')
    markup = await create_admin_manage_kb()
    await message.answer(text, reply_markup=markup)
    await state.set_state(EditCategories.waiting_for_create_category_name.state)


async def confirm_create_category_name(message: Message, state: FSMContext) -> None:
    name = message.text.lower().capitalize()
    if await category_is_exists_check(name):
        text = await get_help_message_content('category already exists')
        await message.answer(text)
    else:
        text = await get_help_message_content('create the category')
        text = text.split()
        text.insert(-1, f'"{name}"')
        text = ' '.join(text) + '?'

        markup = await create_admin_manage_kb(confirm=True)
        await message.answer(text, reply_markup=markup)

        await state.set_data({'category_name': name})
        await state.set_state(EditCategories.waiting_for_create_confirm.state)


async def create_category(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    name = data.get('category_name')

    await db.insert(table='categories', column_values={'category_name': name})

    text = await get_help_message_content('category created')
    markup = await create_admin_edit_kb()
    await message.answer(text, reply_markup=markup)

    await state.reset_data()
    await state.set_state(Edit.waiting_for_action.state)
