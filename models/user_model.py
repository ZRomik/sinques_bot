from peewee import *
from .base_model import BaseModel

class UserModel(BaseModel):
    """
    Модель профиля пользователя
    """
    tg_id = BigIntegerField(index=True, unique=True)
    """идентификатор в телеграм"""
    name = CharField(max_length=150)
    """имя в телеграм"""