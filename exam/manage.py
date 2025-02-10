class Restaurant:
    """创建一个餐厅基类"""
    def __init__(self, restaurant_name):
        """
        初始化餐厅方法
        :param restaurant_name: 餐厅名称
        """
        self.restaurant_name = restaurant_name
        self.menu = {}  # 创建一个空字典，用于存储菜单 （{菜品名称: 价格}
        self.orders = [] # 创建一个空列表，用于存储顾客订单信息 顾客姓名
    def display_menu(self):
        """展示餐厅菜单"""
        # 遍历菜单，打印菜品名称和价格
        for dish_name, price in self.menu.items():
            print("\n餐厅菜单如下：")
            print(f"菜品名称:{dish_name}   价格:{price}元")
    def add_dish(self,dish_name,price):
        """
        添加菜品到菜单
        :param dish_name: 菜品名称
        :param price:菜品价格
        :return:
        """
        # 菜品在菜单中是否存在
        if dish_name not in self.menu:
            self.menu[dish_name] = price
            msg = f'菜品{dish_name}添加成功,价格为{price}元'
            return msg

        else:
            print(f'菜品{dish_name}已经存在！！！！')
    def add_order(self,customer_name,dish_name,quantity):
        """
        添加订单
        :param customer_name:顾客姓名
        :param dish_name:菜品名称
        :param quantity:菜品数量
        :return:
        """
        # # 遍历菜单
        # for d in self.menu:
        #     # 判断菜品是否在菜单中  # print('\n遍历菜单：',{d})
        #     if d not in self.menu:
        #         print(f'菜品{dish_name}不存在菜单中，请重新添加')
        #     else:
        #         self.orders.append((customer_name,dish_name,quantities))
        #     msg = f'\n{customer_name}点了{dish_name}，数量为{quantities}份'
        #     print(msg)
        if dish_name not in self.menu:
            print(f'菜品{dish_name}不存在菜单中，请重新添加')
        else:
            self.orders.append((customer_name, dish_name, quantity))
            msg = f'\n{customer_name}点了{dish_name}，数量为{quantity}份'
            print(msg)
    def display_orders(self):
        """展示顾客订单"""
        print('---顾客订单信息如下：')
        for d in self.orders: # [存储顾客订单信息]
            msg = f'顾客{d[0]}：{d[1]} x 数量为{d[2]}份'
            print(msg)

class FastFoodRestaurant(Restaurant):
    """创建快餐餐厅子类 继承Restaurant类"""
    def __init__(self,restaurant_name):
        super().__init__(restaurant_name)
        self.discounts = {} # 字典，{菜品名称: 折扣后价格}
    def set_discount(self,dish_name,discount_price):
        """
        设置菜品折扣价
        :param dish_name:菜品名称. 在self.menu
        :param discount_price:菜品折扣后的价格
        :return:
        """
        # 判断菜名是否在菜单中
        if dish_name not in self.menu:
            print(f'菜品{dish_name}不存在菜单中，请重新添加')
        else:
            self.discounts[dish_name] = discount_price
            msg = f'\n{dish_name}的折扣价为{discount_price}元'
            print(msg)


def welcome_message(restaurant_name):
    return f'欢迎来到{restaurant_name}餐厅！'


# 实例化餐厅对象
restaurant1 = Restaurant("小王餐厅")
# 添加菜品
restaurant1.add_dish("宫保鸡丁", 30)
restaurant1.add_dish("宫保鸡丁", 30)
restaurant1.add_dish("鱼香肉丝", 25)
# 展示菜单
restaurant1.display_menu()
# 添加订单
restaurant1.add_order("张三", "鱼香肉丝", 1)
# restaurant1.add_order("张三", "鱼香肉丝", 1)
restaurant1.add_order("李四", "宫保鸡丁", 2)
# 展示订单
restaurant1.display_orders()

# 实例化快餐厅对象
FastFoodRestaurant1 = FastFoodRestaurant("麦当劳")
# 设置折扣
FastFoodRestaurant1.set_discount("宫保鸡丁", 23)


# 多态方法调用
print(welcome_message(restaurant1.restaurant_name))
print(welcome_message(FastFoodRestaurant1.restaurant_name))