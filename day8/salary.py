"""
设计一个简单员工系统设计，包括不同类型的员工（如全职员工和兼职员工）。每个员工有不同的薪资计算方法。
1、创建一个 Employee（员工）类，拥有一个抽象方法计算薪资的方法 calculate_salary()。

2、创建一个 FullTimeEmployee（全职员工）类，继承自 Employee 类，实现 calculate_salary() 方法来计算全职员工的薪资。
4、实例化一个 FullTimeEmployee 对象，设置工时为 160，时薪为 100，调用 calculate_salary() 方法计算并打印出全职员工的薪资。

3、创建一个 PartTimeEmployee（兼职员工）类，继承自 Employee 类，实现 calculate_salary() 方法来计算兼职员工的薪资。
5、实例化一个 PartTimeEmployee 对象，设置工时为 80，时薪为 50，调用 calculate_salary() 方法计算并打印出兼职员工的薪资。
"""
class Employee:
    """定义一个员工类"""
    def __init__(self, hour,salary):
        self.hour = hour
        self.salary = salary
    def calculate_salary(self):
        """
        计算薪资
        :return:
        """
        money = self.hour * self.salary
        print(f'全职员工的工资为：{money}元')


class FullTimeEmployee(Employee):
    """定义一个全职员工类 继承员工类"""
    def calculate_salary(self):
        # 继承 父类的方法calculate_salary
        super().calculate_salary()


class PartTimeEmployee(Employee):
    """定义一个兼职员工类 继承员工类"""
    def calculate_salary(self):
        """重写父类 Employee 的方法"""
        money = self.hour * self.salary
        print(f'兼职员工的工资为：{money}元')

# 实例化FullTimeEmployee对象
full_person = FullTimeEmployee(160, 100)
# 调用calculate_salary方法,计算并打印出全职员工的薪资
full_person.calculate_salary()

# 实例化PartTimeEmployee对象
part_person = PartTimeEmployee(80, 50)
# 调用calculate_salary方法，计算并打印兼职员工薪资
part_person.calculate_salary()