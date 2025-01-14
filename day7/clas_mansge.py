"""
实战代码
创建一个 Course 类表示课程，定义私有属性 __name 和 __credit。
提供封装方法，用于设置和获取课程名称及学分。
模拟一个课程管理系统，支持课程的添加、删除和查看。
"""

# 创建Course类
class Course:
    def __init__(self):
        """
        定义私有属性 __name 和 __credit
        :param __name:课程名称
        :param __credit:学分
        """
        self.__name = ''
        self.__credit = 0

    def __str__(self):
        """
        打印课程管理系统
        :return:
        """
        return f'课程名称为：{self.__name}，学分为：{self.__credit}\n'

    def set_course(self,course_name, course_credit):
        """
        设置课程名称及学分
        :param course_name: 课程名称
        :param course_credit: 课程学分
        :return:
        """
        self.__name = course_name
        if  0<= course_credit <=100:
            self.__credit = course_credit
        else:
            print('学分输入有误')
    def get_course(self):
        """
        获取课程名称及学分
        :param self.__name: 课程名称
        :param self.__credit: 课程学分
        :return:
        """
        return self.__name, self.__credit

# 创建课程管理系统
class Management:
    def __init__(self):
        """
        初始化课程管理系统
        :return:
        """
        self.course_lst = [] # 存储课程名称

    def add_course(self, course):
        """
        添加课程
        :param course: 课程名称  就是课程的对象
        :return:
        """
        if course not in self.course_lst:
            self.course_lst.append(course)
            print(f'添加课程{course}成功\n')
        else:
            print(f'课程{course}已存在')

    def del_course(self,course):
        """
            删除课程
            :param self:
            :param course_name: 删除课程名称
            :return:
            """
        if course in self.course_lst:
            self.course_lst.remove(course)
            print(f'删除课程{course}成功\n')
        else:
            print(f'课程{course}不存在')

    def show_course(self):
        """
        显示所有课程
        :param self:
        :return:
        """
        if self.course_lst:
            for course in self.course_lst:
                print(f'显示所有课程名称及学分：{course}')
        else:
            print('当前管理系统中没有课程')

# 获取Course的实例
c1 = Course() # 实例化Course
c1.set_course('python', 9)

c2 = Course()
c2.set_course('java', 8)


# 获取Management的实例
m = Management()
# 添加课程
m.add_course(c1)
m.add_course(c2)
#显示所有课程
m.show_course()

# 删除课程
m.del_course(c1)
#显示所有课程
m.show_course()






