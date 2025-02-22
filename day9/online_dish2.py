class Dish:
    """定义菜品类"""
    def __init__(self,dish_name,dish_price,dish_nums):
        """
        初始化菜品属性
        :param dish_name: 菜品名称
        :param dish_price: 菜品价格
        :param dish_nums: 库存数量
        """
        self.dish_name = dish_name
        self.dish_price = dish_price
        self.dish_nums = dish_nums
    def show_dish(self):
        """展示菜品信息"""
        msg = f'菜品名称：{self.dish_name}，菜品价格：{self.dish_price}元，库存数量：{self.dish_nums}份'
        print(msg)
class Customer:
    """定义顾客类"""
    def __init__(self,customer_name):
        """
        初始化顾客属性
        :param customer_name: 顾客姓名
        """
        self.customer_name = customer_name
        self.order = {} # 订单 键：菜品名称  值：菜品数量
    def show_customer_order(self):
        # 遍历 订单字典
        for o, num in self.order.items():
            msg = f'顾客：{self.customer_name}，点了{num}份{o.dish_name}，单价为{o.dish_price}元'
            print(msg)
class OrderManager:
    """定义订单管理类"""
    def __init__(self):
        self.dish = {}  # 菜品管理：{菜名：菜品对象}
        self.all_orders = {} # 系统订单：{顾客名称：顾客对象}
    def add_dish(self,dish):
       """
       添加菜品
       :param dish:菜品对象
       :return:
       """
       if dish not in self.dish:
           self.dish[dish.dish_name] = dish
           print(f'菜品：{dish.dish_name}已添加')
       else:
           print(f"菜品：{dish.dish_name}已存在")
    def delete_dish(self,dish):
        # 判断菜名是否在菜单中，在的话删除
        if dish.dish_name in self.dish.values():
            self.dish.pop(dish.dish_name)
            print(f'菜品：{dish.dish_name}已删除')
        else:
            print(f'菜品：{dish.dish_name}不存在，请重新输入！！')
    def show_all_dishes(self):
        # 遍历字典
        for dish in self.dish.values():
            print('菜单里有：',dish.dish_name)
    def place_order(self,customer,dish,num):
        """
        顾客下单
        :param customer: 顾客名称
        :param dish: 菜名
        :param num: 数量
        :return:
        """
        # 判断菜名是否在菜单中
        if dish not in self.dish.values():
            print(f'{dish.dish_name}不存在，请重新输入！！')
        elif num > dish.dish_nums:
            print(f'当前下单数量{num}，大于菜品库存数量{dish.dish_nums}')
        else:
            dish.dish_nums -= num  # 菜品库存减少相应下单数量
            customer.order[dish] = num  # 将订单添加到顾客订单中
            self.all_orders[customer.customer_name] = customer  # 将订单添加到系统订单中
            print("下单成功")
            print(f'{customer.customer_name}，{dish.dish_name} x {dish.dish_nums}')
    def amount_order(self, customer):
        """订单总金额 = 数量 * 单价"""
        total = 0
        if customer.order:
            for dish,num in customer.order.items():
                total += dish.dish_price * num
            print(f'顾客{customer.customer_name}，订单总金额为：{total}元')
        else:
            print(f'{customer.customer_name}没有任何订单')

    def show_all_orders(self):
        """展示系统订单"""
        for c, o in self.all_orders.items():
            print(f'顾客{c}：')
            for d,nums in o.order.items():
                print(d.dish_name,nums)



dish1 = Dish('宫保鸡丁', 20, 100)
dish2 = Dish('鱼香肉丝', 20, 100)
dish1.show_dish()
print('-----------------------------------')
customer1 = Customer('张三')
customer1.show_customer_order()
print('-----------------------------------')
om = OrderManager()
om.add_dish(dish1)
om.add_dish(dish1)
om.add_dish(dish2)
om.show_all_dishes()
print('-----------------------------------')
om.place_order(customer1,dish1,90)
customer1.show_customer_order()
print('2222222222222')
om.show_all_dishes()
dish1.show_dish()
# om.delete_dish(dish1)
# om.delete_dish(dish1)
print('-----------------------------------')
om.amount_order(customer1)
print('-----------------------------------')
om.show_all_orders()



