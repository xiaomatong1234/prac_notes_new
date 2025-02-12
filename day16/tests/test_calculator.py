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
    print('模块级别：测试开始',log)
def teardown_module():
    log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('模块级别：测试结束',log)

class TestCalculator:
    def setup_class(self):
        # 实例化 self.calc 实例变量
        self.calc = Calculator()
        print('-----类级别:setup-----')
    def teardown_class(self):
        print("-----类级别:teardown----")

    def setup_method(self):
        log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('方法级别：测试开始', log)
    def teardown_method(self):
        log = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('方法级别：测试结束', log)



    def test_add(self):
        add_result = self.calc.add(1,2)
        assert 3==add_result,f'和为：{add_result}'

    def test_sub(self):
        sub_result = self.calc.sub(2,2)
        assert sub_result == 0, f'差为：{sub_result}'


    def test_mul(self):
        mul_result = self.calc.mul(1,2)
        assert mul_result == 2, f'积为：{mul_result}'


    def test_div(self):
        div_result = self.calc.div(0,1)
        assert div_result == 0, f'除法运算实际结果为{div_result}'
