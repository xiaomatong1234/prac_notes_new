# 定义动物园系统类
class ZooSystem:
    # 初始化属性
    def __init__(self, name,age):
        """
        初始化动物园动物属性
        :param name: 动物姓名
        :param age: 动物年龄
        """
        self.name = name
        self.age = age
    def show_info(self):
        """
        显示动物信息
        :return:
        """
        self.animals_lst = []
        if self.name not in self.animals_lst:
            self.animals_lst.append(self.name)
            print(f'动物园里的动物名称：{self.name}, 动物年龄：{self.age}')
        else:
            print(f'重名了给小动物换个名')

# 定义动物类
class Animals(ZooSystem):
    def eat(self):
        """
        定义动物吃的方法
        :return:
        """
        print(f"{self.name}正在吃食物")
    def run(self):
        """
        定义动物跑的方法
        :return:
        """
        print(f"{self.name}正在跑")

    def catch(self):
        """
        定义动物抓东西的方法
        :return:
        """
        print(f'{self.name}正在抓')

# 定义狗的类
class Dog(Animals):
    # 用 super() 调用父类初始化方法
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color

    def sleep(self):
        """
        定义狗睡觉的方法
        :return:
        """
        print(f"{self.name}正在睡觉")

    def catch(self):
        """
        定义狗抓东西的方法
        :return:
        """
        print(f'{self.name}正在抓')
class Cat(Animals):
    def catch(self):
        """
        定义猫抓东西的方法
        :return:
        """
        print(f'{self.name}正在抓')

# 多肽状态下使用相同的对象名，调用相同的方法
def use_catch(animals):
    animals.catch()
# 创建实例对象 将实例赋值给一个变量
d1 = Dog('旺财', 3, 'yellow')
c1 = Cat('小花', 2, )

# 调用方法
use_catch(d1)
use_catch(c1)

# 创建实例对象
d2 = Dog('哈哈哈', 8, 'white')
c2 = Cat('喵喵', 5)
# 调用方法
d2.show_info()
c2.show_info()
d2.eat()
d2.sleep()



