from models import QuestionnariesModel
from unittest import TestCase
from db_connection import database

class QuestionnariesModelTestCase(TestCase):
    """
    Тестирование модели QuestionnariesModel.
    """
    def setUp(self) -> None:
        database.create_tables([QuestionnariesModel])
        self.range = 15
        self.questionnaries = [
            {
                "name": f"test questionary #{num}",
                "greetings": f"test greetings #{num}",
                "farewell": f"test farewell # {num}",
                "creator": "test user"
            }
            for num in range(self.range)
        ]

    def tearDown(self) -> None:
        for row in QuestionnariesModel.select():
            row.delete().execute()

    def test_create_questionary(self):
        created = QuestionnariesModel.create(
            name = "test questionary",
            creator = "test creator"
        )
        finded = QuestionnariesModel.select().where(
            QuestionnariesModel.name == "test questionary"
        ).get()
        self.assertEqual(
            created,
            finded,
            "Созданный и полученный объекты не равны!"
        )

    def test_create_questionnaries(self):
        with database.atomic():
            QuestionnariesModel.insert_many(self.questionnaries).execute()
        for data in self.questionnaries:
            questionary = QuestionnariesModel.get(
                QuestionnariesModel.name == data["name"]
            )
            self.assertIsNotNone(
                questionary,
                f"Не найдена анкета {data['name']}"
            )