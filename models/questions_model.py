from .base_model import *
from peewee import *
from .questionnaries_model import QuestionnariesModel

class QuestionsModel(BaseModel):
    """
    Модель вопросов анкеты.
    Описывает конкретный вопрос конкретной анкеты.
    """
    text = CharField(max_length=MAX_FIELD_SIZE)
    questionary = ForeignKeyField(QuestionnariesModel, backref="questions", on_delete="CASCADE")
    defined = BooleanField(default=False)

    class Meta:
        db_table = "questions"