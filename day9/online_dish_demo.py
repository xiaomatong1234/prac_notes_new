# 创建 Dish 类：
# - 实例属性：菜品名称、价格、库存数量。
# - 实例方法：展示菜品信息。
#
# 创建 Customer 类：
# - 实例属性：顾客姓名、订单（字典：菜品 -> 数量）。
# - 实例方法：展示顾客订单信息。
#
# 创建 OrderManager 类：
# - 添加菜品、删除菜品、查看所有菜品。
# - 顾客下单（检查菜品库存）。
# - 计算订单总金额。
# - 展示所有订单。


class Dish:
    def __init__(self, dish_name, dish_price, dish_num):
        """
        设置实例属性，菜品名字，价格，库存数量
        :param dish_name:
        :param dish_price:
        :param dish_num:
        """
        self.dish_name = dish_name
        self.dish_price = dish_price
        self.dish_num = dish_num
    def show_dish(self):
        """
        展示 菜品
        :return:
        """
        print(f"{self.dish_name},{self.dish_price},{self.dish_num}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = {}  # 键：菜品对象,值：数量
    def show_customer(self):
        for o, num in self.orders.items():
            print(f"{self.name}已点菜为：{o.dish_name}×{num}")
class OrderManager:
    def __init__(self):
        """
        菜品管理：{菜名：菜品对象}
        订单管理：一客一单 {顾客名字：顾客对象}

        """
        self.dishes = {}
        self.all_orders = {}
    def add_dish(self, dish):
        if dish in self.dishes.values():
            print("菜已存在")
        else:
            self.dishes[dish.dish_name] = dish
            print("菜品添加成功")
    def delete_dish(self, dish):
        if dish not in self.dishes.values():
            print("菜品不存在")
        else:
            self.dishes.pop(dish.dish_name)
            print("菜品删除成功")
    def show_dishes(self):
        for d in self.dishes.values():
            print(d.dish_name)
    def buy_dish(self, customer, dish, num):
        if dish.dish_num < num:
            print("菜品库存不足")
        elif dish.dish_name not in self.dishes:
            print("菜品不存在")
        else:
            # 菜的库存减少对应数量
            dish.dish_num -= num
            # 顾客订单增加对应菜
            customer.orders[dish] = num
            # 系统中增加对应订单
            self.all_orders[customer.name] = customer
            print("下单成功")
    def order_price(self, customer):
        """
        顾客订单总金额
        :return:
        """
        total = 0
        for dish, num in customer.orders.items():
            total += dish.dish_price * num
        print(f"订单总金额为：{total}")
    def show_all_orders(self):
        for c, o in self.all_orders.items():
            print(f"{c}的订单是：")
            for d, num in o.orders.items():
                print(f"{d.dish_name}×{num}")


dish1 = Dish("京酱肉丝", 35, 100)
dish2 = Dish("宫保鸡丁", 40, 100)
customer1 = Customer("小王")
om = OrderManager()
# 展示菜品信息
dish1.show_dish()
#添加菜品
om.add_dish(dish1)
om.add_dish(dish2)
# 重复添加菜品
om.add_dish(dish1)
print("============")
#删除成功
om.delete_dish(dish2)
# 菜不存在
om.delete_dish(dish2)
print("---------")
# 展示系统中的菜品
om.show_dishes()
# 顾客下单
om.buy_dish(customer1, dish1, 100)
# 菜品不存在
om.buy_dish(customer1, dish2, 100)
#菜库存不足
om.buy_dish(customer1, dish1, 1)
print("==========")
#顾客订单金额
om.order_price(customer1)
# 展示所有订单
om.show_all_orders()
