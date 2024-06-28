from peewee import *
from .base_model import BaseModel
from .survey_model import SurveyModel

class QuestionModel(BaseModel):
    """
    Модель вопроса анкеты
    """
    text = TextField()
    predefined = BooleanField(default=False)
    survey = ForeignKeyField(SurveyModel, on_delete="CASCADE", backref="questions")

    class Meta:
        db_table = "questions"