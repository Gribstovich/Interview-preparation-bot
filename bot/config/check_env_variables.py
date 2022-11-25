import os

import dotenv

from bot.misc.custom_exceptions import DotenvFileDoesNotExist, EnvironmentVariableNotSet
from bot.telegraph_pkg import get_telegraph_token


def _get_path_to_dotenv() -> str:
    if not (path_to_dotenv := dotenv.find_dotenv()):
        raise DotenvFileDoesNotExist('Create a bot/config/.env file')
    return path_to_dotenv


def check_env_variables():
    path = _get_path_to_dotenv()
    dotenv.load_dotenv(path)

    for env in ('BOT_TOKEN', 'ADMIN_IDS'):
        if os.getenv(env) in (None, ''):
            raise EnvironmentVariableNotSet(f'Set an environment variable {env} in a {path}')

    if os.getenv('LANGUAGE') not in ('en', 'ru'):
        os.environ['LANGUAGE'] = 'en'
    if os.getenv('PATH_TO_DB') in (None, ''):
        os.environ['PATH_TO_DB'] = 'database/bot.db'
    if os.getenv('TELEGRAPH_TOKEN') in (None, ''):
        os.environ['TELEGRAPH_TOKEN'] = get_telegraph_token()
