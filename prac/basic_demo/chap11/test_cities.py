import unittest
from city_functions import city_country

class TestCities(unittest.TestCase):
    """测试 city_functions.py。"""
    def test_city_country(self):
        """传入简单的城市和国家可行吗？"""
        santiago_chile = city_country('Santiago','Chile',5000000)
        self.assertEqual( santiago_chile,'Santiago,Chile-population 5000000')


if __name__ == '__main__':
    unittest.main()