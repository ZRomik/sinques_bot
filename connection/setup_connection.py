import logging
from setup import read_param
from exceptions import *
from peewee import *

logger = logging.getLogger(__name__)

db_name = read_param("DBNAME")

if not db_name:
    logger.critical("Не указано имя БД. Работа невозможна!")
    raise ImproperlyConfigured("Не указано имя БД. Работа невозможна!")

db_type = read_param("DBTYPE")

database = None

if db_type == "mysql":
    login = read_param("LOGIN")
    pwd = read_param("PWD")
    if not login:
        logger.critical("Не указано имя пользователя для подключения к БД!")
        raise ImproperlyConfigured("Не указано имя пользователя для подключения к БД!")

    if not pwd:
        logger.critical("Не указан пароль пользователя для подключения к БД!")
        raise ImproperlyConfigured("Не указан пароль пользователя для подключения к БД!")

    database = MySQLDatabase()
elif db_type == "postgress":

    login = read_param("LOGIN")
    pwd = read_param("PWD")
    if not login:
        logger.critical("Не указано имя пользователя для подключения к БД!")
        raise ImproperlyConfigured("Не указано имя пользователя для подключения к БД!")

    if not pwd:
        logger.critical("Не указан пароль пользователя для подключения к БД!")
        raise ImproperlyConfigured("Не указан пароль пользователя для подключения к БД!")
    database = PostgresqlDatabase()
else:
    database = SqliteDatabase(db_name)
