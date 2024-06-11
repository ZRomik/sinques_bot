from .base_model import *
from peewee import *

class UserModel(BaseModel):
    """
    Модель пользователя.
    Описывает идентификатор и имя пользователя (ник) в телеграм
    """
    tg_id = BigIntegerField(unique=True)
    name = CharField(max_length=MAX_FIELD_SIZE)

    class Meta:
        db_table = "users"