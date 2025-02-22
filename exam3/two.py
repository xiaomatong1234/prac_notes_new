"""
设计一个动物类系统

基类 Animal 包含动物的名称和一个抽象方法 speak()，
子类 Dog 和 Cat 分别表示狗和猫类，每个子类需要实现 speak() 方法，
输出该动物特有的叫声。
请使用适当的面向对象特性来实现该系统，使其能够支持不同动物的多态行为。
"""
class Animals:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f'{self.name}正在叫')
class Dog(Animals):
    def speak(self):
        super().speak()
        print(f'{self.name}正在汪汪叫\n')

class Cat(Animals):
    def speak(self):
        super().speak()
        print(f'{self.name}正在喵喵叫')
    def eat(self):
        print(f'{self.name}正在吃东西')
class Frog:
    def speak(self,animal):
        print('------多态------')
        animal.speak()


if __name__ == '__main__':
    dog = Dog('狗')
    dog.speak()

    cat = Cat('猫')
    cat.speak()
    cat.eat()

    frog = Frog()
    frog.speak(dog)