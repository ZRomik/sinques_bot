from playhouse.reflection import generate_models
from db_connection import database
from unittest import TestCase
from setup import read_param

class DatabaseTestCase(TestCase):
    """
    Тестирование подключения к БД.
    """
    def setUp(self) -> None:
        database.close()

    def tearDown(self) -> None:
        if read_param("DBTYPE") != "sqlite":
            models = generate_models(database).items()
            for _, table in models:
                database.drop_tables([table], cascade=True)
        database.close()

    def test_connect_to_database(self):
        if database is not None:
            if read_param("DBTYPE") != "sqlite":
                connected = database.connect(reuse_if_open=True)
                self.assertTrue(
                    connected,
                    "Неудалось подключиться к БД"
                )