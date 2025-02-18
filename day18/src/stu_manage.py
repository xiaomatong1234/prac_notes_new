import sys  # 读取文件
"""
实战：学生管理系统单元测试实战
学生管理系统：
随着学校的规模变大，对应的学员回越来越多，相应的管理越来越难。
学员信息管理系统主要是对学员的各种信息进行管理，能够让学员的信息关系变得科学化、系统化和规范化。
题目要求
实现一个学生管理系统 实现一个基于命令行的学生管理系统，具备以下功能：

添加新学生信息：输入学号、姓名、年龄和性别，添加到学生列表中。
通过学号修改学生信息：根据输入的学号修改对应学生的姓名、年龄和性别。
通过学号删除学生信息：输入学号，删除对应的学生信息。
通过姓名删除学生信息：输入姓名，删除所有匹配姓名的学生信息。
通过学号查询学生信息：输入学号，查询并显示对应学生的信息。
通过姓名查询学生信息：输入姓名，查询并显示所有匹配学生的信息。
显示所有学生信息：显示当前系统中所有学生的信息。
退出系统：退出学生管理系统。
测试需求
第一步 - 完成学生管理系统代码的编写。 - 使用 pytest 编写增加、修改、查询（id和name）、删除（id和name）学生的测试用例 - 使用标签为测试用例制定合适的优先级。 - 实现增加学生用例的参数化 - 生成 allure 报告。
第二步
针对增加学生的测试用例使用yaml实现数据驱动。
第三步
使用fixtrue 完善学生修改的测试用例 前置步骤为添加学生，后置步骤为删除学生。

"""

class StudentManage:
    def __init__(self):
        self.students_lst = []

    def get_stu_id(self):
        stu_id = int(input('请输入学生id(格式：1001)：\n'))
        return stu_id

    def get_stu_name(self):
        stu_name = input('请输入学生姓名：\n')
        return stu_name

    def get_stu_age(self):
        stu_age = int(input('请输入学生年龄：\n'))
        return stu_age

    def get_stu_gender(self):
        stu_gender = input('请输入学生性别【male/female】：\n')
        return stu_gender

    # 添加学生信息

    def add_student(self, stu_id, stu_name, stu_age, stu_gender):
        stu = Student(stu_id, stu_name, stu_age, stu_gender)
        self.students_lst.append(stu)
        # return self.students_lst
        return '学生信息添加成功！！'
        # print(f'学生信息添加成功！！\n')
        # return self.students_lst.append(stu)
    # 修改学生信息
    def modify_student(self,stu_id,stu_name,stu_age,stu_gender):
        for stu in self.students_lst:
            if stu_id == stu.stu_id:
                stu.stu_name = stu_name
                stu.stu_age = stu_age
                stu.stu_gender = stu_gender
                print('学生信息修改成功')
                return '学生信息修改成功'
                # return f'学生id{stu.stu_id}信息修改成功'
                # print(f'学生id{stu.stu_id}信息修改成功')
                # return stu
        print(f'学生id{stu_id}信息不存在')
        # except ValueError:
        #     print('输入的编号非正整数')
    # 通过学号删除学生信息
    def remove_id_student(self,stu_id):
        for stu in self.students_lst:
            if stu_id == stu.stu_id:
                self.students_lst.remove(stu)
                # print(f'学生id{stu.stu_id}信息删除成功！！')
                # return stu
                print(f'学生id{stu.stu_id}信息删除成功！！')
                return '通过学号删除学生信息成功！'
        print(f'学生id{stu_id}不存在')
    # 通过姓名删除学生信息
    def remove_name_student(self,stu_name):
        # stu_name = input('请输入要删除的学生姓名：')
        for stu in self.students_lst:
            if stu.stu_name == stu_name:
                self.students_lst.remove(stu)
                print(f'{stu.stu_name}信息删除成功！！')
                # return stu
                # print('通过姓名成功删除学生信息')
                return '成功删除学生信息'
        print(f'输入的学生姓名{stu_name}不存在')
    #通过姓名查询学生信息
    def query_name_student(self,stu_name):
        # stu_name = input('请输入要查询的学生姓名：')
        for stu in self.students_lst:
            if stu.stu_name == stu_name:
                print(f'显示学生信息：{stu.stu_id},{stu.stu_name},{stu.stu_age},{stu.stu_gender}')
                return f'显示学生信息：{stu.stu_id},{stu.stu_name},{stu.stu_age},{stu.stu_gender}'
        print(f'学生{stu_name}信息不存在')
    # 通过学号查询学生信息
    def query_id_student(self,stu_id):
        # stu_id = int(input('请输入要查询的学生id(格式：1001)：'))
        for stu in self.students_lst:
            if stu.stu_id == stu_id:
                print(f'显示学生信息：{stu.stu_id},{stu.stu_name},{stu.stu_age},{stu.stu_gender}')
                return f'显示学生信息：{stu.stu_id},{stu.stu_name},{stu.stu_age},{stu.stu_gender}'
        print(f'学生{stu_id}信息不存在')
    # 显示所有学生信息
    def show_student(self):
        for stu in self.students_lst:
            print(f'显示所有学生信息：{stu.stu_id},{stu.stu_name},{stu.stu_age},{stu.stu_gender}')
            # return stu
    # 删除所有学生信息
    def del_students(self):
        self.students_lst.clear()
        return self.students_lst


    def menu(self):
        while True:
            print('请选择下列操作：\n'
                  '1.添加新学生信息\n'
                  '2.通过学号修改学生信息\n'
                  '3.通过学号删除学生信息\n'
                  '4.通过姓名删除学生信息\n'
                  '5.通过学号查询学生信息\n'
                  '6.通过姓名查询学生信息\n'
                  '7.显示所有学生信息\n'
                  '8.退出系统')
            choice = int(input('请选择操作编号：\n'))
            if choice == 1:
                # 添加新学生信息
                stu_id = self.get_stu_id()
                stu_name = self.get_stu_name()
                stu_age = self.get_stu_age()
                stu_gender = self.get_stu_gender()
                self.add_student(stu_id, stu_name, stu_age, stu_gender)

            elif choice == 2:
                # 通过学号修改学生信息
                stu_id = self.get_stu_id()
                stu_name = self.get_stu_name()
                stu_age = self.get_stu_age()
                stu_gender = self.get_stu_gender()
                self.modify_student(stu_id,stu_name,stu_age,stu_gender)

            elif choice == 3:
                # 通过学号删除学生信息
                stu_id = self.get_stu_id()
                self.remove_id_student(stu_id)
            elif choice == 4:
                # 通过姓名删除学生信息
                stu_name = self.get_stu_name()
                self.remove_name_student(stu_name)
            elif choice == 5:
                # 通过学号查询学生信息
                stu_id = self.get_stu_id()
                self.query_id_student(stu_id)
            elif choice == 6:
                # 通过姓名查询学生信息
                stu_name = self.get_stu_name()
                self.query_name_student(stu_name)
            elif choice == 7:
                # 显示所有学生信息
                self.show_student()
            elif choice == 8:
                # 退出系统
                print('已退出系统！')
                sys.exit(0)
            else:
                print('输入的操作编号无效！')


class Student:
    def __init__(self, stu_id, stu_name, stu_age, stu_gender):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_age = stu_age
        self.stu_gender = stu_gender

# if __name__ == '__main__':
#     stu_manage = StudentManage()
#     stu_manage.menu()
