class Dish:
    """定义菜品类"""
    def __init__(self,dish_id, dish_name, dish_price, dish_nums):
        """
        初始化菜品属性
        :param dish_name: 菜品编号
        :param dish_name: 菜品名称
        :param dish_price: 菜品价格
        :param dish_nums: 库存数量
        """
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.dish_price = dish_price
        self.dish_nums = dish_nums
    def show_dish(self):
        """
        展示菜品信息
        :return:
        """
        show_dish_msg = f"编号：{self.dish_id}，菜品名称：{self.dish_name}，菜品价格：{self.dish_price}，菜品库存：{self.dish_nums}"
        print(show_dish_msg)

class Customer:
    """定义顾客类"""
    def __init__(self, customer_name):
        """
        初始化顾客属性
        :param customer_name:
        """
        self.customer_name = customer_name
        self.order = {}     # 键：菜品对象 值： 数量
    def show_customer_order(self, dish, num):
        """
        展示顾客点餐信息
        :param dish: 菜品信息
        :param num: 菜品数量
        :return:
        """
        show_customer_order_info = f"顾客：{self.customer_name}，点了{num}份{dish.dish_name}，单价为{dish.dish_price}元"
        print(show_customer_order_info)

class OnlineDish:
    """定义在线点餐系统类"""
    def __init__(self):
        self.dishes = {} # 定义一个菜单字典
        self.orders = {} # 键：customer对象  值：顾客点餐信息self.dishes
    def add_dish(self,dish):
        """
        添加菜品
        :param dish: 菜品名称
        :return:
        """
        # 判断菜品是否已经存在在字典中 不存在，添加到字典中，已存在原有数量+1
        if dish.dish_id not in self.dishes:
            self.dishes[dish.dish_id] = dish
            print(f"菜品：{dish.dish_name}添加成功，新添加{self.dishes[dish.dish_id].dish_nums}份")
        else:
            print(f"菜品：{dish.dish_name}已存在，添加失败！！！")
    def delete_dish(self,dish):
        """
        删除菜品
        :param dish: 菜品名称
        :return:
        """
        # 判断菜品是否在字典中，在则删除，不在则提示
        if dish.dish_id in self.dishes:
            del self.dishes[dish.dish_id]
            print(f'{dish.dish_nums}份{dish.dish_name}菜品，删除成功')
        else:
            print(f'{dish.dish_name}菜品不存在,删除失败')
    def show_all_dish(self):
        """
        展示所有菜品
        :return:
        """
        # 遍历字典，输出菜品信息
        for d in self.dishes.values():
            print(f"菜品名称：{d.dish_name}")
            print(f'菜品价格：{d.dish_price}')
            print(f'菜品数量：{d.dish_nums}\n')
    def place_order(self,customer,dish,num):
        """顾客下单"""
        # 判断菜品库存是否大于0
        if self.dishes[dish.dish_id].dish_nums > 0:
            self.dishes[dish.dish_id].dish_nums -= num
            customer.order[dish]= num # 获取顾客下单
            self.orders[customer] = customer.order  # 系统中订单增加顾客下单

            print(f"顾客{customer.customer_name}下单成功，{dish.dish_name}下单数量为：{num}份，{dish.dish_name}剩余库存{self.dishes[dish.dish_id].dish_nums}份")
        else:
            print(f"顾客{customer.customer_name}下单失败，{dish.dish_name}库存不足")
    def total_amount(self,dish, num):
        """
        计算订单总金额
        :param num: 数量
        :param dish: 菜品
        :return:
        """
        total_amount = num * self.dishes[dish.dish_id].dish_price
        print('订单总金额为：',total_amount)
    def show_all_orders(self):
        """
        展示所有订单
        :return:
        """
        for c in self.orders.keys():  # c:顾客对象.
            for o,k in c.order.items(): #o 菜品对象，k  数量
                # print(f"订单信息：{o}")
                print(f"顾客：{c.customer_name}，订单信息：{o.dish_name},{k}份")


# 实例化菜品对象
dish1 = Dish(1,"宫保鸡丁", 20, 1)
dish2 = Dish(2,"小鸡炖蘑菇", 30, 2)
# 展示菜品信息
dish1.show_dish()
dish2.show_dish()

print('🦍🦍🦍🦍🦍🦍🦍')

# 实例化顾客类
customer1 = Customer("张三")
customer2 = Customer("李四")
# 展示顾客订单信息
customer1.show_customer_order(dish1,1)
customer2.show_customer_order(dish2,2)

print('🦊🦊🦊🦊🦊🦊🦊')
# 实例化在线点餐系统
od = OnlineDish()
# 添加菜品
od.add_dish(dish1)
od.add_dish(dish1)
od.add_dish(dish2)
# 删除菜品
# od.delete_dish(dish1)
# od.delete_dish(dish1)
# 展示所有菜品
od.show_all_dish()
# 顾客下单菜品
od.place_order(customer1,dish1,1)
od.place_order(customer1,dish1,1)
# 计算订单总金额
od.total_amount(dish1,1)
od.total_amount(dish2,2)
# 添加订单
# od.add_order(customer1)
# od.add_order(customer1)
od.show_all_orders()


# 在类里面用self来调用类里面的属性和方法，在其它类里面使用实例对象/参数来来调用类里面的属性和方法