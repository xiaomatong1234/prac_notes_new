from prac.chap9.chap9_4 import Restaurant


class IceCreamStand(Restaurant):
    """创建一个冰淇凌小店的类"""
    def __init__(self, restaurant_name, cuisine_type):
        """重写父类的__init__方法"""
        super().__init__(restaurant_name, cuisine_type) # 调用父类的__init__方法
        self.flavors = [] # 冰淇淋口味列表

    def show_icecream(self):
        """显示冰淇淋口味"""

        for flavors in self.flavors: # 遍历冰淇淋口味列表
            if self.flavors:
                print(f'冰淇淋口味：{flavors}')
            else:
                print('没有冰淇淋口味')

# 创建IceCreamStand的实例
icecream = IceCreamStand('冰淇淋小店', '冰淇淋')
icecream.flavors = ['草莓', '巧克力', '香草'] # 设置冰淇淋口味列表
icecream.describe_restaurant()
icecream.show_icecream()

