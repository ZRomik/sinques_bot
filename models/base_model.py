from db_connection import database
from peewee import *

class BaseModel(Model):
    """
    Общая модель данных
    """
    id = BigAutoField(primary_key=True)

    class Meta:
        database = database