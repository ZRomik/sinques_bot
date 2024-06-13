from models import UserModel, QuestionnariesModel, CompletedModel
from unittest import TestCase
from db_connection import database

class CompletedModelTestCase(TestCase):
    """
    Тестирование модели CompletedModel
    """
    def setUp(self) -> None:
        database.create_tables(
            [
                UserModel,
                QuestionnariesModel,
                CompletedModel
            ]
        )
        self.user = UserModel.create(
            tg_id = 1,
            name = "test user"
        )
        self.questionary = QuestionnariesModel.create(
            name = "test questionary",
            creator = self.user,
            ready = True
        )

    def tearDown(self) -> None:
        for row in QuestionnariesModel.select():
            row.delete().execute()
        for row in UserModel.select():
            row.delete().execute()


    def test_create_comleted_questionary(self):
        created = CompletedModel.create(
            questionary = self.questionary,
            user = self.user
        )
        finded = CompletedModel.get(
            CompletedModel.questionary == self.questionary
        )
        self.assertEqual(
            created,
            finded,
            "Созданный и полученный объекты не равны!"
        )