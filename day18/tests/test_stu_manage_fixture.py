import allure
import pytest


from day18.tests.conftest import get_yaml

@allure.feature('学生信息管理系统')
class TestStuManage:
    @allure.story('添加学生信息用例')
    @allure.title('添加了三条学生信息')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(
        "stu_id,stu_name,stu_age,stu_gender",get_yaml()
    )
    def test_add_student(self,stu_id,stu_name,stu_age,stu_gender,fixture):
        """测试添加学生信息"""
        result = fixture.add_student(stu_id,stu_name,stu_age,stu_gender)
        # length = len(self.student.students_lst)
        # print(result)
        # print(length)
        # assert length == 3
        assert result ==  '学生信息添加成功！！'

    @allure.story('修改学生信息用例')
    @allure.title('修改ID=1001的学生信息')
    @pytest.mark.parametrize(
        "stu_id,stu_name,stu_age,stu_gender", [
            (1001,'zhangsan4',20,'male'),
        ],
        ids=['ID=1001']
    )
    def test_modify_student(self,stu_id,stu_name,stu_age,stu_gender,fixture):
        """测试通过学号修改学生信息"""
        result = fixture.modify_student(stu_id,stu_name,stu_age,stu_gender)
        # print(result)
        assert result == '学生信息修改成功'

    @pytest.mark.parametrize(
        "stu_id",[1001],
        ids= ['ID=1001']
    )
    def test_query_id_student(self,stu_id,fixture):
        """通过学号查询学生信息"""
        result = fixture.query_id_student(stu_id)
        # print(result)
        assert result == "显示学生信息：1001,zhangsan4,20,male"
    @allure.story('通过姓名查询学生信息')
    @allure.title('查询姓名为wangwu的学生信息')
    @pytest.mark.parametrize(
        "stu_name", ['wangwu'],
        ids=['name = wangwu']
    )
    def test_query_name_student(self,stu_name,fixture):
        """通过姓名查询学生信息"""
        result = fixture.query_name_student(stu_name)
        # print(result)
        assert result == '显示学生信息：1002,wangwu,21,male'
    @pytest.mark.skip
    @allure.story('测试通过学号删除学生信息')
    @allure.title('删除ID=1001的学生信息')
    @pytest.mark.parametrize(
        "stu_id", [1001],
        ids=['del_ID=1001']
    )
    def test_remove_id_student(self,stu_id,fixture):
        """测试通过学号删除学生信息"""
        result = fixture.remove_id_student(stu_id)
        # print(result)
        assert result == '通过学号删除学生信息成功！'

    @pytest.mark.skip
    @allure.story('测试通过姓名删除学生信息用例')
    @allure.title('删除wangwu的个人信息')
    @pytest.mark.parametrize(
        "stu_name", ['wangwu'],
        ids=['del_Name=wangwu']
    )
    def test_remove_name_student(self,stu_name,fixture):
        """测试通过姓名删除学生信息"""
        result = fixture.remove_name_student(stu_name)
        assert result == '成功删除学生信息'



