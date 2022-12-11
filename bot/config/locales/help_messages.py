from bot.config import load_config

_messages = {'admin mode': {'en': 'You are in administrator mode',
                            'ru': 'Вы в режиме администатора'},
             'select action': {'en': 'Select an action',
                               'ru': 'Выберите действие'},
             'send category name': {'en': 'Send category name',
                                    'ru': 'Отправьте название категории'},
             'category already exists': {'en': 'Category already exists',
                                         'ru': 'Категория уже сущестувует'},
             'create the category': {'en': 'Create the category ',
                                     'ru': 'Создать категорию '},
             'category created': {'en': 'Category created',
                                  'ru': 'Категория создана'},
             'select category to delete': {'en': 'Select category to delete',
                                           'ru': 'Выберите категорию для удаления'},
             'category does not exist': {'en': 'Category does not exist',
                                         'ru': 'Категории не существует'},
             'delete the category': {'en': 'Delete the category ',
                                     'ru': 'Удалить категорию '},
             'category deleted': {'en': 'Category deleted',
                                  'ru': 'Категория удалена'}
             }


async def get_help_message_content(header: str) -> str:
    if isinstance(header, str):
        try:
            lang = load_config().tg_bot.language
        except AttributeError:
            lang = 'en'

        result = _messages.get(header.lower(), {}).get(lang.lower(), 'Localization error')
        return result
