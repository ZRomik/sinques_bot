from peewee import *
from db_connection import database

class BaseModel(Model):
    """
    Общая модель данных.
    Описывает идентификатор записи, настраивает имя БД и порядок сотртировки.
    """
    id = BigAutoField(primary_key=True)

    class Meta:
        database = database
        order_by = [id]