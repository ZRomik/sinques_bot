from models import AnswersModel, UserModel, QuestionsModel, QuestionnariesModel
from unittest import TestCase
from db_connection import database

class AnswersModelTestCase(TestCase):
    """
    Тестирование модели AnswersModel
    """
    def setUp(self) -> None:
        database.create_tables(
            [
                UserModel,
                QuestionnariesModel,
                QuestionsModel,
                AnswersModel
            ]
        )
        self.user = UserModel.create(
            tg_id = 1,
            name = "test user"
        )
        self.questionary = QuestionnariesModel.create(
            name = "test questionary",
            creator = self.user
        )
        self.question = QuestionsModel.create(
            text = "test question",
            questionary = self.questionary
        )

    def tearDown(self) -> None:
        for row in QuestionnariesModel.select():
            row.delete().execute()
        for row in UserModel.select():
            row.delete().execute()
        for row in AnswersModel.select():
            row.delete().execute()

    def test_create_answer(self):
        created = AnswersModel.create(
            text = "test answer",
            question = self.question,
            user = self.user
        )
        finded = AnswersModel.get(
            AnswersModel.question == self.question
        )
        self.assertEqual(
            created,
            finded,
            "Созданный и полученный объекты не равны!"
        )