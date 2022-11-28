import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import load_config, check_env_variables
from database import create_db
from filters import IsAdmin
from handlers import register_admin_handlers, register_user_handlers


def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)


def register_all_handlers(dp: Dispatcher):
    register_admin_handlers(dp)
    register_user_handlers(dp)


async def main():
    check_env_variables()
    config = load_config()
    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    register_all_filters(dp)
    register_all_handlers(dp)

    create_db()

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
