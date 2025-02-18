import pytest
import yaml

from day18.src.stu_manage import StudentManage

def get_yaml():
    with open('../data/stu_info.yml', 'r') as file:
        file_content = yaml.safe_load(file)
    return file_content


@pytest.fixture(scope="class")
def fixture():
    student = StudentManage()
    yield student
    student.remove_id_student(stu_id=1001)
    # student.del_students() # 删除所有学生信息