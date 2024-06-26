from peewee import *
from .base_model import BaseModel
from datetime import datetime

class SurveyModel(BaseModel):
    """
    Модель анкеты
    """
    name = CharField(max_length=150, unique=True, index=True)
    """Название анкеты"""
    creator = CharField(max_length=150)
    """Создатель анкеты"""
    created = TimestampField(default=datetime.now)
    """Дата создания анкеты"""
    greetings = TextField(null=True)
    """Приветственное сообщение"""
    farewell = TextField(null=True)
    """Прощальное сообщение"""

    class Meta:
        db_table = "surveys"