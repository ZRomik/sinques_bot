from peewee import attrdict

CONNECTION_ERROR = attrdict(
    DBNAME_NOT_EXISTS_MSG = "Не указано имя БД.",
    DBTYPE_NOT_EXISTS_MSG = "е указан тип БД.",
    USERNAME_NOT_EXISTS_MSG = "Не указано имя пользователя БД.",
    PASSWORD_NOT_EXISTS_MSG = "Не указан пароль пользователя БД.",
    SERVER_ADDRESS_NOT_EXISTS = "Не указан адрес сервера БД.",
    SERVER_PORT_NOT_EXISTS = "Не указан адрес порта для подключения к БД.",
)