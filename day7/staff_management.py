class Employee: # 创建基类
    def __init__(self, name, age, salary):
        """
        初始化实例属性
        :param name: 员工姓名
        :param age: 员工年龄
        :param salary: 薪水
        """
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        """
        工作方法
        :return:
        """
        print(f'{self.name} is working...')

class Manager(Employee): # 继承Employee类
    def __init__(self, name, age, salary):
        """
        初始化实例属性
        :param name:
        :param age:
        :param salary:
        :param team:
        """
        super().__init__(name, age, salary)
        self.work_team = []

    def manager_team(self):
        """
        管理团队方法
        :return:
        """
        print(f'{self.name}is managing_teams{self.work_team}.')
    # 团队中增加员工

class Developer(Employee): # 继承Employee类
    def __init__(self, name, age, salary,lan):
        """
        初始化实例属性
        :param name:
        :param age:
        :param salary:
        """
        super().__init__(name, age, salary)
        self.language = lan

    def show_coding(self):
        """
        增加编程语言属性
        :return:
        """
        print(f'{self.name} is coding in {self.language}')

# 获取两个子类的对象
manager = Manager('Tom', 30, 5000)
developer = Developer('Jerry', 25, 3000,'Python')

# 创建团队

# 调用方法
manager.work()
manager.manager_team()

developer.work()
developer.show_coding()
