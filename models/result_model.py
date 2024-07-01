from datetime import datetime
from peewee import *
from .base_model import BaseModel
from .survey_model import SurveyModel
from .user_model import UserModel

class ResultModel(BaseModel):
    """
    Модель результата анкеты.
    """
    survey = ForeignKeyField(SurveyModel, on_delete="CASCADE", backref="results")
    completed = DateField(default=datetime.now)
    user = ForeignKeyField(UserModel, backref="result", unique=True, on_delete="SET NULL", null=True)

    class Meta:
        db_table = "results"