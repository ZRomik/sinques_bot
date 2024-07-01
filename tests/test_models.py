from peewee import *
from models import *
from unittest import TestCase
from db_connection import database

class UserModelTestCase(TestCase):
    """
    Тестирование модели UserModel
    """
    def setUp(self) -> None:
        super().setUp()
        database.create_tables([UserModel])
        self.correct_data = {
            "tg_id": 1,
            "name": "test user"
        }
        self.incorrect_data = {
            "name": "test user"
        }

    def tearDown(self) -> None:
        UserModel.delete().execute()

    def test_user_model_create_correct(self):
        """
        Тестирование создания модели без ошибки
        """
        user = UserModel.create(**self.correct_data)
        usr = UserModel.get(UserModel.tg_id==self.correct_data["tg_id"])
        self.assertEqual(
            user,
            usr,
            "Профиили не одианаковы!"
        )

    def test_model_create_incorrect(self):
        """
        Тестирование создания модели с ошибкой
        :return:
        """
        with self.assertRaises(
            expected_exception=IntegrityError,
            msg="Исключение не возбуждено"
        ):
            UserModel.create(**self.incorrect_data)

class SurveyModelTestCase(TestCase):
    """
    Тестирование модели SurveyModel
    """
    def setUp(self) -> None:
        super().setUp()
        database.create_tables([SurveyModel])

    def tearDown(self) -> None:
        SurveyModel.delete().execute()
        database.drop_tables([SurveyModel], recursive=True)