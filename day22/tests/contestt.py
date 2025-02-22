import pytest
import yaml

from day22.src.stu_system import Student, School


def get_yaml():
    with open("stu.yaml") as file:
        data = yaml.safe_load(file)
    return data

@pytest.fixture(scope='class')
def initiate():
    print('\n------------------开始测试------------------')
    student = Student('zhangsan')
    student = Student('lisi')
    school = School()

