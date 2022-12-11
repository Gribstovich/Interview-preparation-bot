from aiogram.dispatcher.filters.state import State, StatesGroup


class Edit(StatesGroup):
    waiting_for_action = State()


class EditCategories(StatesGroup):
    waiting_for_create_category_name = State()
    waiting_for_delete_category_name = State()
    waiting_for_create_confirm = State()
    waiting_for_delete_confirm = State()


class CreateTask(StatesGroup):
    waiting_for_category_name = State()
    waiting_for_task_name = State()
    waiting_for_question = State()
    waiting_for_answer = State()
    waiting_for_photo = State()
    waiting_for_confim = State()


class DeleteTask(StatesGroup):
    waiting_for_category_name = State()
    waiting_for_task_name = State()
    waiting_for_confirm = State()
