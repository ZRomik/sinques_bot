from peewee import *
from exceptions import CONNECTION_ERROR, ImproperlyConfigured
from setup import read_param
import logging
from .db_types import *

logger = logging.getLogger(__name__)

db_name = read_param("DBNAME")

if not db_name:
    logger.critical(CONNECTION_ERROR.DBNAME_NOT_EXISTS_MSG)
    raise ImproperlyConfigured(CONNECTION_ERROR.DBNAME_NOT_EXISTS_MSG)

db_type = read_param("DBTYPE")

if not db_type:
    logger.critical(CONNECTION_ERROR.DBTYPE_NOT_EXISTS_MSG)
    raise ImproperlyConfigured(CONNECTION_ERROR.DBTYPE_NOT_EXISTS_MSG)

database = None

if db_type == POSTGRES:

    # Проверяем параметры подключения
    username = read_param("LOGIN")

    if not username:
        logger.critical(CONNECTION_ERROR.USERNAME_NOT_EXISTS_MSG)
        raise ImproperlyConfigured(CONNECTION_ERROR.USERNAME_NOT_EXISTS_MSG)

    userpass = read_param("USERPASS")

    if not userpass:
        logger.critical(CONNECTION_ERROR.PASSWORD_NOT_EXISTS_MSG)

    host = read_param("HOST")

    if not host:
        logger.critical(CONNECTION_ERROR.SERVER_ADDRESS_NOT_EXISTS)
        raise ImproperlyConfigured(CONNECTION_ERROR.SERVER_ADDRESS_NOT_EXISTS)

    port = read_param("PORT")

    # Создаем новое подключение
    database = PostgresqlDatabase(
        database=db_name,
        user=username,
        password=userpass,
        host=host
    )
    database.connect()

elif db_type == MYSQL:
    pass

else:
    pass