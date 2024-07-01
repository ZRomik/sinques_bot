from peewee import *
from db_connection import database

class BaseModel(Model):
    """
    Общая модель данных.
    """
    id = BigAutoField(primary_key=True)
    """Идентификатор записи"""

    class Meta:
        database = database