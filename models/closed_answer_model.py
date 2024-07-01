from peewee import *
from .base_model import BaseModel
from .question_model import QuestionModel

class ClosedAnswerModel(BaseModel):
    """
    Модель закрытого ответа на вопрос
    """
    text = TextField()
    question = ForeignKeyField(QuestionModel, on_delete="CASCADE", backref="closed")

    class Meta:
        db_table = "c_answers"