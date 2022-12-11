from bot.config import load_config

_buttons = {'newsletter': {'en': 'newsletter', 'ru': 'Рассылка'},
            'help': {'en': 'help', 'ru': 'Помощь'},
            'user mode': {'en': 'User mode', 'ru': 'Режим пользователя'},
            'edit tasks': {'en': 'Edit tasks', 'ru': 'Редактировать задачи'},
            'create category': {'en': 'Create category', 'ru': 'Создать категорию'},
            'delete category': {'en': 'Delete category', 'ru': 'Удалить категоирю'},
            'create task': {'en': 'Create task', 'ru': 'Создать задачу'},
            'delete task': {'en': 'Delete task', 'ru': 'Удалить задачу'},
            'step back': {'en': 'Step back', 'ru': 'Назад'},
            'confirm': {'en': 'Confirm', 'ru': 'Подтвердить'}
            }


async def get_button_name(en_btn_name: str) -> str:
    if isinstance(en_btn_name, str):
        try:
            lang = load_config().tg_bot.language
        except AttributeError:
            lang = 'en'

        result = _buttons.get(en_btn_name.lower(), {}).get(lang.lower(), 'Localization error')
        return result.lower().capitalize()
