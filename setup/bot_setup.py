from aiogram import Bot, Dispatcher
from setup import read_param
from exceptions import *
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logger = logging.getLogger(__name__)

token = read_param("TOKEN")
if not token:
    logger.critical("Не указан токен бота. Работа невозможна.")
    raise ImproperlyConfigured("Не указан токен бота. Работа невозможна.")

mems = MemoryStorage()

bot = Bot(
    token=token
)

dp = Dispatcher(
    bot=bot,
    storage=mems
)