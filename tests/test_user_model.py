from models import UserModel
from unittest import TestCase
from db_connection import database
from peewee import *

class UserModelTestCase(TestCase):
    """
    Тестирование модели UserModel.
    """
    def setUp(self) -> None:
        database.create_tables([UserModel])

    def tearDown(self) -> None:
        for user in UserModel.select():
            user.delete().execute()

    def test_create_user(self):
        created = UserModel.create(
            tg_id = 1,
            name = "test user"
        )
        finded = UserModel.get(
            name = "test user"
        )
        self.assertEqual(
            created,
            finded
        )

    def test_create_duplicate_user(self):
        first = UserModel.create(
            tg_id = 1,
            name = "one"
        )
        with self.assertRaises(
            expected_exception=IntegrityError,
            msg="Исключение не возбуждено!"
        ):
            second = UserModel.create(
                tg_id = 1
            )