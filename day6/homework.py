"""
实例方法：通过类的实例调用
需要一个实例对象作为第一个参数（通常是 self），并且可以访问类的实例属性和调用其他实例方法

可以访问和修改实例的状态。
不能在没有创建类的实例的情况下调用
"""
class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return self.value

obj = MyClass(10)
print(obj.instance_method())  # 输出: 10

"""
类方法：通过类名或实例调用

需要一个类对象作为第一个参数（通常是 cls），可以通过 @classmethod 装饰器定义
只能访问类属性，不能访问实例属性
"""
class MyClass:
    class_variable = 'class value3'


    @classmethod
    def class_method(cls):
        print(cls.class_variable)




# 通过类名调用
MyClass.class_method() # 输出: class value

# 通过实例调用
obj = MyClass()
obj.class_method()    # 输出: class value


