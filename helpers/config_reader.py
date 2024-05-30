import os
from dotenv import load_dotenv


def read_param(key: str):
    load_dotenv()
    """
    Функция для чтения параметров конфигурации.
    Считывает значение указанного параметра файла конфигурации и возвращает его.
    Если параметра ен существует, возвращает None
    :param key: (str) - имя параметра
    :return: str | None
    """
    return os.getenv(key)