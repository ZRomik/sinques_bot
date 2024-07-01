from unittest import TestCase
from peewee import *
from models import *
from db_connection import database

class DatabaseTestCase(TestCase):
    """
    Тестирование БД
    """
    def setUp(self) -> None:
        super().setUp()
        self.tables = [
            UserModel,
            SurveyModel,
        ]

    def tearDown(self) -> None:
        database.drop_tables(self.tables)

    def test_create_tables(self):
        """
        Тестирование создания моделей.
        """
        for table in self.tables:
            database.create_tables([table])