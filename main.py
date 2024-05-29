import logging
from aiogram.utils import executor
from setup import *
from helpers import read_param
from os import path

logger = logging.getLogger(__name__)

async def startup(_):
    logger.info("Бот запущен")

async def shutdown(_):
    logger.info("Завершение работы бота.")

def main():
    logger.info("Подготовка к запуску бота.")
    # отключение логгеров библиотек, чтобы не засорять консоль
    logging.getLogger("requests").setLevel(logging.ERROR)
    logging.getLogger("aiogram").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    if dp:
        logger.info("Запуск бота...")
        executor.start_polling(
            dispatcher=dp,
            on_startup=startup,
            on_shutdown=shutdown,
            timeout=3,
            skip_updates=True
        )

if __name__ == "__main__":
    main()