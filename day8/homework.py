"""
定义一个英雄类：
- 此英雄类需要包含 姓名、 血量、 攻击力
- 有一个方法为讲台词。
- 根据英雄类，实例化不同的英雄对象：每个英雄需要在实例化的时候，就有自己的姓名、攻击力、血量。
- 每个英雄的血量不可以直接被获取或者修改。

定义法师类英雄
- 法师类：
  1. 法师类继承于 Hero 类。
  2. 法师类多了魔力的属性
  3. 法师类多了一个放技能的方法。
"""
from day8.fight import fight

class Hero:
    """定义一个英雄类"""

    def __init__(self, name, blood, attack):
        """
        初始化英雄 属性
        :param name: 姓名
        :param blood: 血量
        :param attack: 攻击力
        """
        self.name = name
        self._blood = blood  # 定义血量为保护属性，不可直接被获取或修改
        self.attack = attack
        self.lines = None

    def speak_lines(self, lines):
        """
        定义一个英雄的台词的方法
        :return:
        """
        self.lines = lines
        msg = f'英雄{self.name}说："{self.lines}"!!!!\n'
        return msg


class Mage(Hero):
    """定义一个法师类 继承英雄类"""
    def __init__(self, name, blood, attack, magic):
        """
        重写父类的初始化方法，增加魔法属性
        :param name: 姓名
        :param blood: 血量
        :param attack: 攻击力
        :param magic: 魔法
        """
        super().__init__(name, blood, attack)  # 调用父类的初始化方法，初始化父类的属性
        self.magic = magic  # 定义魔法属性

    def skill(self):
        """
        定义法师的专有的技能方法
        :return:
        """
        msg =f'魔法师：{self.name}，血量：{self._blood}，攻击力：{self.attack}，释放了{self.magic}魔法技能!'
        return msg

class Warrior(Hero):
    """定义一个战士类 继承英雄类"""
    def __init__(self, name, blood, attack, magic):
        """
        重写父类的初始化方法，增加魔法属性
        :param name: 姓名
        :param blood: 血量
        :param attack: 攻击力
        :param magic: 魔法
        """
        super().__init__(name, blood, attack)  # 调用父类的初始化方法，初始化父类的属性
        self.magic = magic  # 定义魔法属性

    def skill(self):
        """
        定义法师的专有的技能方法
        :return:
        """
        msg = f'战士：{self.name}，血量：{self._blood}，攻击力：{self.attack}，释放了{self.magic}攻击技能!\n'
        return msg



# 实例化法师属性
mage = Mage('诸葛亮', 20, 100, '火球术')
# 实例化战士属性
warrior = Warrior('赵云', 0, 100, '龙腾虎跃')
# 调用英雄类的台词方法
print(mage.speak_lines('我是诸葛孔明，我有一计，可让敌人望风而逃'))
print(warrior.speak_lines('我是赵子龙，我有一计，可让敌人望风而逃'))


# 调用fight函数，实现多轮打斗
fight(mage, warrior, 20)

