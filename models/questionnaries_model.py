from .base_model import *
from peewee import *
from datetime import datetime

class QuestionnariesModel(BaseModel):
    """
    Модель названий анкет.
    Описывает конкретную анкету в списке анкет.
    """
    name = CharField(max_length=MAX_FIELD_SIZE, index=True)
    greetings = CharField(max_length=MAX_FIELD_SIZE, null=True)
    farewell = CharField(max_length=MAX_FIELD_SIZE, null=True)
    created_at = TimestampField(default=datetime.now)
    creator = CharField(max_length=MAX_FIELD_SIZE, index=True)
    ready = BooleanField(default=False)

    class Meta:
        db_table = "questionnaries"