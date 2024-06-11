from unittest import TestCase
from models import QuestionsModel, QuestionnariesModel
from db_connection import database

class QuestionsModelTestCase(TestCase):
    """
    Тестирование модели QuestionsModel.
    """
    def setUp(self) -> None:
        database.create_tables([QuestionsModel, QuestionnariesModel])
        self.questionary = QuestionnariesModel.create(
            name = "test questionary",
            creator = "test creator"
        )
        self.range = 150
        self.questions = [
            {
                "text": f"test text {num}",
                "questionary": self.questionary
            }
            for num in range(self.range)
        ]

    def tearDown(self) -> None:
        for row in QuestionnariesModel.select():
            row.delete().execute()
        for row in QuestionsModel.select():
            row.delete().execute()

    def test_create_question(self):
        created = QuestionsModel.create(
            text = "test question",
            questionary = self.questionary,

        )
        finded = QuestionsModel.get(
            QuestionsModel.text == "test question"
        )
        self.assertEqual(
            created,
            finded,
            "Созданный и полученный объекты не равны!"
        )

    def test_create_questions(self):
        with database.atomic():
            QuestionsModel.insert_many(self.questions).execute()
        for question in self.questions:
            qst = QuestionsModel.get(
                QuestionsModel.text == question["text"]
            )
            self.assertIsNotNone(
                qst,
                f"Отсутствует вопрос {question['text']}"
            )