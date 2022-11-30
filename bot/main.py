import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import load_config
from database import create_db
from filters import IsAdmin
from handlers import register_admin_handlers, register_user_handlers


def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)


async def register_all_handlers(dp: Dispatcher):
    await register_admin_handlers(dp)
    await register_user_handlers(dp)


async def main():
    config = load_config()
    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    register_all_filters(dp)
    await register_all_handlers(dp)

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
