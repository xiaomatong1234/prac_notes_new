# 创建Animals基础类
class Animals:
    # 定义属性
    def __init__(self,name, age,color, weight):
        self.name = name
        self.age = age
        self._color = color # 保护属性
        self.__weight = weight # 私有属性
    # 定义方法 公有方法
    def run(self):
        print(f'{self.name} age is {self.age}, color is {self._color}, weight is {self.__weight}\n')
    def eat(self):
        print(f'调用父类方法：{self.name} is eating\n')

# 创建Dog子类 继承Animals
class Dog(Animals):
    def eat(self):
        super().eat() # 使用 super() 调用父类方法
        print(f'子类重写父类方法：：{self.name} is water\n')

# 创建Cat子类 继承Animals
class Cat(Animals):
    # # 继承初始化
    # def __init__(self,name, age,color, weight):
    #     super().__init__(name, age,color, weight) # 使用 super() 调用父类方法
    #     self.aged = age

    def sleep(self):
        print(f'{self.name} is sleeping\n')



# 创建对象
dog = Dog('旺财', 3, 'white', 10)
# 调用父类的方法
dog.run()
# 调用子类自己的eat方法
dog.eat()


# 创建猫的对象
cat = Cat('小花', 2, 'black', 5)
# 调用父类的方法
cat.run()
# 调用子类自己的方法
cat.sleep()