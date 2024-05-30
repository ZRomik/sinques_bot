from db_connection import database
from unittest import TestCase
from helpers import read_param

class DatabaseTestCase(TestCase):
    """
    Тестирование подключения к БД.
    """
    def setUp(self) -> None:
        database.close()

    def tearDown(self) -> None:
        database.close()

    def test_connect_to_database(self):
        if database is not None:
            if read_param("DBTYPE") != "sqlite":
                connected = database.connect(reuse_if_open=True)
                self.assertTrue(
                    connected,
                    "Неудалось подключиться к БД"
                )