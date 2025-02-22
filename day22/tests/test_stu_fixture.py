import allure
import pytest
import yaml

from day22.src.stu_system import Student, School
def get_yaml():
    with open("stu.yaml") as file:
        data = yaml.safe_load(file)
    return data


@allure.feature('学生成绩统计系统')
class TestStudentSystem:
    """
    1、验证成绩添加
    2、验证平均成绩的计算
    3、验证班级平均成绩的计算
    4、验证无效成绩的处理
    """

    def setup_class(self):
        print('\n------------------开始测试------------------')
        self.student = Student('zhangsan')
        self.student = Student('lisi')
        self.school = School()
    @allure.title('正向流程_验证成绩添加')
    @pytest.mark.P0
    @pytest.mark.parametrize(
        "subject,score",
        [('math',0),('chinese',24),('english',25)]
    )
    def test_add_score(self,subject,score,initiate):
        result = initiate.student.add_score(subject,score)
        assert result == '科目、分数添加成功'

    @allure.title('正向流程_验证平均成绩计算')
    @pytest.mark.P0
    def test_average_score(self,initiate):
        result = initiate.student.average_score()
        assert result == "平均成绩计算成功"

    @allure.title('正向流程_验证班级平均成绩的计算')
    @pytest.mark.P0
    @pytest.mark.parametrize(
        "subject",
        ['math','chinese','english']
    )
    def test_class_average(self,subject,initiate):
        result = initiate.school.class_average(subject)
        assert result == '全班学生各科平均分计算成功'


    @allure.title('无效成绩处理')
    @pytest.mark.P1
    @pytest.mark.parametrize(
        "subject,score",
        [('math', -1), ('chinese', 101), ('english', -0.11)]
    )
    def test_add_score_001(self,subject,score,initiate):
        result = initiate.student.add_score(subject,score)
        assert result == 'ValueError("分数无效，分数必须小于0或大于100")'




