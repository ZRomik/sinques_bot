from .base_model import BaseModel
from peewee import *

class UserModel(BaseModel):
    """
    Модель профиля пользователя.
    """
    tg_id = BigIntegerField(unique=True, index=True)
    name = CharField(max_length=150)