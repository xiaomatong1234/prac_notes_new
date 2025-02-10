# from random import randint
# randint(1,6)
# print(randint(1,6))
#
# from random import choice
# player = ('charles','eli','iik')
# fist = choice(player)
# print(fist)
from random import randint

"""
练习9-13：骰子　
创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。
编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。
创建一个6面的骰子再掷10次。

创建一个10面的骰子和一个20面的骰子，再分别掷10次。
"""
class Die:
    """表示骰子的类"""
    def __init__(self,sides=6):
        """
        初始化骰子属性
        :param sides:骰子面数
        """
        self.sides = sides
    def roll_die(self):
        # 返回位于1和骰子面数的随机数
        return randint(1, self.sides)

# 创建一个6面的骰子，再掷10次并显示结果
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("一个6面骰子掷10次的结果为：")
print(results)

# 创建一个10面的骰子，再掷10次并显示结果
d10 = Die(10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("一个10面骰子掷10次的结果为：")
print(results)

# 创建一个20面的骰子，再掷10次并显示结果
d20 = Die(10)
results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("一个20面骰子掷10次的结果为：")
print(results)