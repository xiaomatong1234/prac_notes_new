import math

# 创建基础类Shape
class Shape:
    # 定义area方法
    def area(self):
        """
        计算图形的面积，要求子类实现具体的计算逻辑
        :return:
        """
        pass

# 创建子类 Circle
class Circle(Shape):
    def __init__(self,r):
        # 圆的半径
        self.r = r
    def area(self):
        print('圆形的面积是：', math.pi * self.r ** 2)

# 创建子类Rectangle
class Rectangle(Shape):
    def __init__(self, w, h):
        # 矩形的长、宽
        self.w = w
        self.h = h

    # 重写父类的方法
    def area(self):
        print('矩形的面积是：', self.w * self.h)

# 多肽：不同的对象调用同一个方法
shapes = [Circle(5), Rectangle(4, 5)]
for shape in shapes:  # shape 是图形对象
    shape.area()

# # 创建实例对象 将实例赋值给一个变量
# c = Circle(5)
# r = Rectangle(4, 5)
# 调用方法
# c.area()
# r.area()