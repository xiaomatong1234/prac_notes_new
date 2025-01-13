"""
课堂练习
定义一个商品类，包含 商品名称 和 商品价格 两个属性，
实现商品类的对象描述方法和添加到购物车方法
定义一个购物车类，包含一个商品列表 属性，和 添加商品 及 显示所有商品 两个方法
"""

# 定义一个商品类
class Product:
    # 实例属性推荐定义在构造方法
    def __init__(self, name, price):
        self.name = name
        self.price = price
    # 商品类的对象描述方法
    def __str__(self):
       return  f"商品名称：{self.name},商品价格：{self.price}"
    # 添加到购物车方法
    def add_car(self,car):
        """添加商品到购物车"""
        car.add_product(self)

# 定义一个购物车类
class ShoppingCar:
    def __init__(self):
        # 定义商品列表
        self.goods_lst = []

    #添加商品
    def add_product(self, product):
        self.goods_lst.append(product)
        print(f'添加商品{product}到购物车')

    # 显示所有商品
    def show_products(self):
        for product in self.goods_lst:
            print(f'显示所有商品：{product}')

# 创建商品实例对象
product1 = Product('苹果', 5500)
product2 = Product('华为', 5000)

# 打印商品信息
print(product1)
print(product2)

# 创建购物车对象
car = ShoppingCar()

# 添加商品到购物车
car.add_product(product1)
car.add_product(product2)
product2.add_car(car)

# 显示所有商品
car.show_products()






