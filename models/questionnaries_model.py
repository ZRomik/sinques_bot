from .base_model import BaseModel
from peewee import *
from datetime import datetime

class QuestionnariesModel(BaseModel):
    """
    Модель названий анкет.
    Описывает конкретную анкету в списке анкет.
    """
    name = CharField(max_length=150, index=True)
    greetings = CharField(max_length=150, null=True)
    farewell = CharField(max_length=150, null=True)
    created_at = TimestampField(default=datetime.now)
    creator = CharField(max_length=150, index=True)

    class Meta:
        db_table = "questionnaries"