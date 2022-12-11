from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot import database as db
from bot.config.locales import get_help_message_content
from bot.keyboards import create_categories_kb, create_admin_manage_kb, create_admin_edit_kb
from bot.services import category_is_exists_check
from bot.states.admin_states import Edit, EditCategories


async def delete_category_button(message: Message, state: FSMContext) -> None:
    text = await get_help_message_content('select category to delete')
    markup = await create_categories_kb()
    await message.answer(text, reply_markup=markup)
    await state.set_state(EditCategories.waiting_for_delete_category_name.state)


async def confirm_delete_category_name(message: Message, state: FSMContext) -> None:
    name = message.text
    if await category_is_exists_check(name):
        text = await get_help_message_content('delete the category')
        text = text.split()
        text.insert(-1, f'"{name}"')
        text = ' '.join(text) + '?'

        markup = await create_admin_manage_kb(confirm=True)
        await message.answer(text, reply_markup=markup)

        await state.set_data({'category_name': name})
        await state.set_state(EditCategories.waiting_for_delete_confirm.state)
    else:
        text = await get_help_message_content('category does not exist')
        await message.answer(text)


async def delete_category(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    name = data.get('category_name')

    categories = await db.fetchall(table='categories', columns=['rowid', 'category_name'])
    row_id = [category.get('rowid') for category in categories if category.get('category_name') == name][0]
    await db.delete(table='categories', row_id=row_id)

    text = await get_help_message_content('category deleted')
    markup = await create_admin_edit_kb()
    await message.answer(text, reply_markup=markup)

    await state.reset_data()
    await state.set_state(Edit.waiting_for_action.state)
