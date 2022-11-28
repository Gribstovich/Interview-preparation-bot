from bot.config import load_config

_messages = {'start_admin': {'en': 'You are in administrator mode',
                             'ru': 'Вы в режиме администатора'}
             }


async def get_help_message_content(header: str) -> str:
    if isinstance(header, str):
        try:
            lang = load_config().tg_bot.language
        except AttributeError:
            lang = 'en'

        result = _messages.get(header.lower(), {}).get(lang.lower(), 'Localization error')
        return result
