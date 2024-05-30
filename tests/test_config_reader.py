from unittest import TestCase
from helpers import read_param

class ReadParamTestCase(TestCase):
    """
    Тестирование функци read_param.
    """
    def test_read_param_param_exists(self):
        """
        тестирование функции read_param для существующего параметра.
        :return: None
        """
        db_type = read_param("DBTYPE")
        self.assertIsNotNone(
            db_type,
            "Полученная строка не содержит значения!"
        )

    def test_read_param_param_not_exists(self):
        """
        Тестирование функции read_param для несуществующего параметра
        :return: None
        """
        val = read_param("param")
        self.assertIsNone(
            val,
            "Результат функции не None!"
        )