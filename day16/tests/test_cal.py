"""
课堂练习
测试 Calculator 类，该类包含基本的数学运算方法：加法、减法、乘法和除法。
将使用 Pytest 框架来进行单元测试，并展示如何在不同的级别（模块、类、函数）应用 setup 和 teardown。
在模块级别，我们需要打印一些日志，标明模块测试的开始和结束。
每个测试类的开始时，创建一个新的计算器实例，并为类的每个测试方法提供该实例。
为每个测试方法开始和结束打印一些日志。

"""
from datetime import datetime

import pytest

from day16.src.calculator import Calculator

def setup_module():
    log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('模块级别：测试开始','\n',log)
def teardown_module():
    log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('模块级别：测试结束','\n',log)

class TestCalculator:
    def setup_class(self):
        # 实例化 self.calc 实例变量
        self.calc = Calculator()
        print('-----类级别:setup-----')
    def teardown_class(self):
        print("-----类级别:teardown----")

    def setup_method(self):
        log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('方法级别：测试开始', '\n', log)
    def teardown_method(self):
        log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('方法级别：测试结束', '\n', log)

    @pytest.mark.parametrize(

        "test_input,expected",
        [
        ["1+2", 3],
        ["3+2", 5]
        ],
        ids = ["add_1+2=3","add_3+2=5"]
    )
    def test_add(self, test_input, expected):
        assert eval(test_input) == expected, f'和为：{expected}'


    @pytest.mark.parametrize(
        "test_input,excepted",
        [
            ["2-1",1],
            ["3-2",1]
        ],
        ids = ["sub_2-1=1","sub_3-2=1"]
    )
    def test_sub(self,test_input, excepted):
        assert eval(test_input) == excepted, f'差为：{excepted}'

    @pytest.mark.parametrize(
        "test_input,excepted",
        [
            ["2*1", 2],
            ["3*2", 6]
        ],
        ids=["mul_2*1=1", "mul_3*2=6"]
    )
    def test_mul(self,test_input,excepted):
        assert eval(test_input) == excepted, f'积为：{excepted}'

    @pytest.mark.parametrize(
        "test_input,excepted",
        [
            ["2//1", 2],
            ["3//2", 1]
        ],
        ids=["div_2//1=2", "div_3//2=1"]
    )
    def test_div(self,test_input,excepted):
        assert eval(test_input)==excepted, f'除法运算实际结果为{excepted}'
