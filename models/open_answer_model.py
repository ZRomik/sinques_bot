from .base_model import BaseModel
from peewee import *
from .question_model import QuestionModel
from .user_model import UserModel
from datetime import datetime

class OpenAnswerModel(BaseModel):
    """
    Модель открытого ответа на вопрос
    """
    question = ForeignKeyField(QuestionModel, on_delete="CASCADE", backref="answer")
    text = TextField()
    user = ForeignKeyField(UserModel, on_delete="CASCADE", backref="answers")
    answered = DateField(default=datetime.now)