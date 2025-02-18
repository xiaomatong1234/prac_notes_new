import pytest
import yaml

from day18.src.stu_manage import StudentManage

def get_yaml():
    with open('../data/stu_info.yml', 'r') as file:
        file_content = yaml.safe_load(file)
    return file_content

class TestStuManage:
    def setup_class(self):
        self.student = StudentManage()
    def teardown_method(self):
        print('清空所有学生信息！！')
        self.student.del_students()

    @pytest.mark.parametrize(
        "stu_id,stu_name,stu_age,stu_gender",get_yaml()
    )
    def test_add_student(self,stu_id,stu_name,stu_age,stu_gender):
        """测试添加学生信息"""
        result = self.student.add_student(stu_id,stu_name,stu_age,stu_gender)
        # length = len(self.student.students_lst)
        # print(result)
        # print(length)
        # assert length == 3
        assert result ==  '学生信息添加成功！！'

    @pytest.mark.parametrize(
        "stu_id,stu_name,stu_age,stu_gender", [
            (1001,'zhangsan4',20,'male')
        ]
    )
    def test_modify_student(self,stu_id,stu_name,stu_age,stu_gender):
        """测试通过学号修改学生信息"""
        result = self.student.modify_student(stu_id,stu_name,stu_age,stu_gender)
        # print(result)
        assert result == '学生信息修改成功'

    def test_remove_id_student(self,stu_id):
        """测试通过学号删除学生信息"""
        result = self.student.remove_id_student(stu_id)
        assert result == '通过学号删除学生信息成功！'
        pass
    def test_remove_name_student(self,stu_name):
        """测试通过姓名删除学生信息"""
        result = self.student.remove_name_student(stu_name)

        assert result == '成功删除学生信息'
        pass

    def test_query_id_student(self,stu_id):
        """通过学号查询学生信息"""
        result = self.student.query_id_student(stu_id)
        assert result == '成功删除学生信息'

        pass
    def test_query_name_student(self):
        """通过姓名查询学生信息"""
        pass

    def test_show_all_students(self):
        """展示所有学生信息"""
        pass
