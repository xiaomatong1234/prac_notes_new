import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """测试模块employee"""
    def setUp(self):
        """创建一个 Employee 实例，以便在测试中使用"""
        self.employee = Employee('lili',6000)
    def test_give_default_raise(self):
        """测试使用默认的年薪增加量是否可行。"""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 11000)
    def test_give_custom_raise(self):
        """测试自定义年薪增加量是否可行。"""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 7000)

if __name__ == '__main__':
    unittest.main()