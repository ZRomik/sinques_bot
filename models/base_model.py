from peewee import *

class BaseModel(Model):
    """
    Общая модель данных.
    """
    id = BigAutoField(primary_key=True)
    """Идентификатор записи"""