"""
课堂练习
创建一个 Person 类，定义私有属性 __name 和 __age。
提供封装方法 set_name、set_age 和 get_name、get_age。
添加一个实例方法 introduce，打印出类似 “我叫张三，今年25岁” 的信息。
"""
class Person:
    def __init__(self):
        """
        定义私有属性 __name 和 __age
        :param name:
        :param age:
        """
        self.__name = ""
        self.__age = 0

    def set_name(self,name):
        """
        定义公有方法 set_name
        设置私有的name属性
        :param name: 姓名的值
        :return:
        """
        self.__name = name

    def set_age(self, age):
        """
        定义公有方法 set_age
        设置私有的age属性
        :param age: 年龄的值
        :return:
        """
        if age > 0:
             self.__age = age
        else:
            print('年龄不合法')


    def get_name(self):
        """
        定义公有方法 get_name
        :return: 获取姓名
        """
        return self.__name
    def get_age(self):
        """
        定义公有方法 get_age
        获取私有的age属性
        :return: 获取年龄
        """
        return self.__age

    def introduce(self):
        """
        定义实例方法
        :return: 打印 “我叫张三，今年25岁”
        """
        print(f'我叫{self.__name}，今年{self.__age}岁')

# 获取Person类的实例
p = Person()
# 调用set_name
p.set_name('章三')
# 调用set_age
p.set_age(-9)

# 调用实例方法
p.introduce()
# 获取对象的姓名和年龄
print('p的姓名为：',p.get_name(),'p的年龄为：',p.get_age())







