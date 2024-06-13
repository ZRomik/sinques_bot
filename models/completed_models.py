from .base_model import BaseModel
from peewee import *
from .user_model import UserModel
from .questionnaries_model import QuestionnariesModel
from datetime import datetime

class CompletedModel(BaseModel):
    """
    Модель завершенной анкеты.
    Определяет связь между пользователем и пройденной анкетой, а также дату завершения анкетирования.
    """
    questionary = ForeignKeyField(QuestionnariesModel, backref="completed", on_delete="CASCADE")
    user = ForeignKeyField(UserModel, backref="completed", on_delete="CASCADE")
    completed = TimestampField(default=datetime.now)

    class Meta:
        db_table = "completed"