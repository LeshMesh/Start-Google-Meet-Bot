import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers import start
from handlers import create_meet

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

load_dotenv(find_dotenv())


async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(create_meet.router)

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
