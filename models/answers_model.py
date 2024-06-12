from .base_model import BaseModel
from .questions_model import QuestionsModel
from .user_model import UserModel
from peewee import *
from datetime import datetime

class AnswersModel(BaseModel):
    """
    Модель ответов на вопросы анкеты.
    Описывает текст ответа на вопрос анкеты.
    """
    text = CharField(max_length=500)
    question = ForeignKeyField(QuestionsModel, unique=True, backref="answers")
    user = ForeignKeyField(UserModel, unique=True, backref="answers")
    answer_date = TimestampField(default=datetime.now)

    class Meta:
        db_table = "answers"