from connection import database
from unittest import TestCase
from os import path
from setup import read_param

class DatabaseTestCase(TestCase):
    """
    Тестирование подключения к БД.
    """
    def test_database_exists(self):
        db_name = read_param("DBNAME")
        database.connection()
        self.assertTrue(
            path.exists(db_name)
        )