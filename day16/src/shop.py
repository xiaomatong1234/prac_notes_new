"""
实战思路
电商平台的购物车是用户在购物过程中临时存放商品的地方，用户可以在购物车中查看商品、添加商品、删除商品，并计算商品的总价，最后可以进行结算。

测试要求：
使用 pytest 框架测试以下功能：添加商品到购物车。删除商品从购物车中。计算购物车总价是否正确。
使用 setup 和 teardown 来管理测试环境。
使用 pytest 参数化 来编写测试用例，测试不同商品的添加和删除操作。
每个测试用例都需要使用 断言 来验证结果。
"""
# 商品类
class Product:
    def __init__(self,name,price):
        """
        初始化
        :param name: 商品名称
        :param price: 价格
        """
        self.name = name
        self.price = price
        # 商品类的对象描述方法
    # def __str__(self):
    #     return f"商品名称：{self.name},商品价格：{self.price}"

    # 添加商品到购物车
    def shopcart(self,car):
        car.add_product(self)


# 购物车类
class ShoppingCart:
    def __init__(self):
        self.product_lst = []
        self.price_lst = []
    # 添加商品
    def add_product(self,product):
        self.product_lst.append(product)
        print(f'\n添加商品 {product.name} 到购物车')


    # 删除商品
    def remove_product(self,product):
        if product in self.product_lst:
            self.product_lst.remove(product)
            print(f'\n商品{product.name}从购物车中移除')
        else:
            print(f'商品{product.name}在购物车中不存在')

    # 计算商品总价
    def calculate_total(self):
        for product in self.product_lst:
            self.price_lst.append(product.price)
        print('商品价格列表为：',self.price_lst,'')
        total_amount = 0
        for price in self.price_lst:
                total_amount += price
        print(f'商品总价为：{total_amount}')
        return total_amount

    # 查看商品信息
    def get_info(self):
        for product in self.product_lst:
            print(f'商品名称：{product.name},商品价格：{product.price}')
    # 清空购物车
    def clear_cart(self):
        self.product_lst.clear()
        print('清空购物车！！')
        # print(self.product_lst)



# p = Product('apple',100)
# p1=Product('banana',200)
# p2 = Product('cherry',300)
#
# s = ShoppingCart()
# s.add_product(p)
# s.add_product(p1)
# s.add_product(p2)
# s.get_info()
# s.calculate_total()
# s.remove_product(p)
# s.clear_cart()

