from .base_model import BaseModel
from peewee import *
from datetime import datetime

class SurveyModel(BaseModel):
    """
    Модель анкеты
    """
    name = CharField(max_length=150, index=True, unique=True)
    creator = CharField(max_length=150)
    created = DateField(default=datetime.now)
    greetings = TextField( null=True)
    farewell = TextField(null=True)

    class Meta:
        db_table = "surveys"