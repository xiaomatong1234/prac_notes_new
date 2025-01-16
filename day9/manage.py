import re

class Course:
    """创建一个课程类"""
    def __init__(self,course_name, course_id, max_nums,current_nums):
        """
        # 初始化课程信息
        :param course_name: 课程名称
        :param course_id: 课程编号
        :param max_nums: 课程容量（最大选课人数）
        :param current_nums: 已选人数
        """
        self.course_name = course_name
        self.course_id = course_id
        self.max_nums = max_nums
        self.current_nums = current_nums
    def show_course(self):
        """展示课程信息"""
        course_msg = f"课程名称：{self.course_name}，课程编号：{self.course_id}，课程容量：{self.max_nums}，已选课人数：{self.current_nums}"
        print(course_msg)
    @staticmethod
    def verify_course_id(course_id):
        """
        验证课程编号是否合法（必须是以 "C" 开头的 5 位字母和数字组合）
        :param course_id: 课程id
        :return:
        """
        pattern = r"^C[A-Za-z0-9]{4}"
        if re.fullmatch(pattern, course_id):
            print(f"课程编号合法：{course_id}")
        else:
            print("课程编号不合法，请重新输入！")

class Student:
    """创建一个学生类"""
    def __init__(self,student_name,student_id):
        """
        初始化学生属性
        :param student_name: 学生姓名
        :param student_id: 学号
        """
        self.student_name = student_name
        self.student_id = student_id
        self.selected_course = []  # 已选课程列表 存放课程对象
    def show_student(self):
        """展示学生信息"""
        selected_course_name = self.selected_course
        for c in selected_course_name:
            selected_course_name.append(c)
        student_msg = f"学生姓名：{self.student_name}，学生编号：{self.student_id}，已选课程：{selected_course_name}"
        print(student_msg)
    @staticmethod
    def verify_student_id(student_id):
        """验证学号是否合法"""
        pattern = r"^[0-9]{8}$"
        if re.fullmatch(pattern, student_id):
            print(f"学号合法：{student_id}")
        else:
            print("学号不合法，请重新输入！")

class CourseManager:
    """创建一个课程管理类"""
    def __init__(self):
        self.course_list = [] #  定义字典，键：课程编号，值：课程对象
        self.student_list = [] # 定义字典，键：学生编号，值：课程学生对象

    def add_course(self,course):
        """添加课程   # course 是课程对象"""
        # 判断添加的课程是否在课程列表中
        if course in self.course_list :
            print(f"【{course.course_name}课程】已存在，请重新添加课程")
        else:
            self.course_list .append(course)
            print(f'成功添加【{course.course_name}课程】!!!!')
    def delete_course(self,course):
        """删除课程"""
        # 判断删除的课程是否在课程列表中
        if course in self.course_list :
            self.course_list .remove(course)
            print(f'成功删除【{course.course_name}课程】!!!!')
        else:
            print(f"【{course.course_name}课程】不存在，删除失败！！！")
    def show_all_courses(self):
        """展示所有课程"""
        # 遍历课程列表
        for course in self.course_list :
            print(f'展示所有的课程：{course.course_name}')
    def add_student(self,student):
        """添加学生"""
        # 判断添加的学生是否在学生列表中
        if student not in self.student_list:
            self.student_list.append(student)
            msg = f'成功添加{student.student_name}学生!!!!'
            print(msg)
        else:
            msg = f"{student.student_name}学生已存在，请重新添加学生"
            print(msg)
    def delete_student(self,student):
        """删除学生"""
        # 判断删除的学生是否在学生列表中
        if student in self.student_list:
            self.student_list.remove(student)
            print(f'成功删除{student.student_name}学生!!!!')
        else:
            print(f"{student.student_name}学生不存在，删除失败！！！")
    def show_all_students(self):
        """展示所有学生"""
        # 遍历学生列表
        for student in self.student_list:
            print(f'展示所有的学生：{student.student_name}')
    def select_course(self,course,student):
        """学生选课"""
        # 判断是否到达最大选课人数
        if course.current_nums >= course.max_nums:
            msg = f"{course.course_name}课程已达到最大人数，无法选课"
            print(msg)
        else:
            # 判断学生是否已经选过该课程
            if course in student.selected_course:
                print(f'学生{student.student_name}已选过【{course.course_name}课程】，请重新选择课程')
            else:
                student.selected_course.append(course) # 将课程添加到学生选课列表中
                for course in self.course_list :
                    course.current_nums += 1
                selected_msg = f'{student.student_name}学生选课成功，已选【{course.course_name}课程】'
                course_nums_msg = f'目前【{course.course_name}课程】的选课人数为{course.current_nums}, 最大选课人数为{course.max_nums}'
                print(selected_msg)
                print(course_nums_msg)

    def quit_course(self,course,student):
        """学生退课"""
        # 判断学生是否选过课
        if len(self.course_list ) == 0:
            print(f'学生{student.student_name}没有选过课，无法退课')
        else:
            # 判断学生要退的课是否在其已选课程列表中
            if course in student.selected_course:
                self.course_list.remove(course)
                course.current_nums -= 1 # 当前选课人数减1
                # course.max_nums += 1 # 最大选课人数加1
                quit_msg = f'{student.student_name}学生退课成功，已退【{course.course_name}课程】'
                course_nums_msg= f'目前【{course.course_name}课程】的选课人数为{course.current_nums}, 最大选课人数为{course.max_nums}'
                print(quit_msg)
                print(course_nums_msg)
            else:
                quit_msg = f'学生{student.student_name}没有选过【{course.course_name}课程】，无法退课'
                print(quit_msg)


course1 = Course("python","Clas1",10,2)
course2 = Course("java","Clas2",2,0)
student1 = Student('李四',18181818)
student2 = Student('张三',18)



course1.show_course() # 查看课程信息
course2.show_course()
course1.verify_course_id("Clas1") # 验证课程id是否合法
course2.verify_course_id("Clas2")





cm = CourseManager()

cm.add_student(student1)
cm.add_student(student2)
cm.show_all_students()

cm.add_course(course1)
cm.add_course(course2)
cm.show_all_courses()

# cm.quit_course(course1,student1)
cm.select_course(course1,student1)
# cm.quit_course(course1,student1)
student1.show_student()
student2.show_student()
student1.verify_student_id('18181818')

student1.show_student()
student2.show_student()













