class Restaurant:
    """创建Restaurant的类"""
    def __init__(self,restaurant_name,cuisine_type):
        """
        初始化实例属性
        :param restaurant_name: 饭店名称
        :param cuisine_type:菜系
        """
        self.restaurant_name= restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """
        创建描述饭店的方法
        :return: 打印restaurant_name、cuisine_type
        """
        msg = f'饭店名称是：{self.restaurant_name},菜系有：{self.cuisine_type}'
        print(msg)
    def open_restaurant(self):
        """
        创建饭店开业的方法
        :return: 打印餐厅正在营业
        """
        msg = f'{self.restaurant_name}正在营业'
        print(msg)
    def set_number_served(self,number_served):
        """
        设置就餐人数
        :param number_served: 就餐人数
        :return:
        """
        self.number_served = number_served
        print(f'饭店就餐人数为：{self.number_served}') #
    def increment_number_served(self, add_numbers):
        """
        增加就餐人数
        :return:
        """
        self.number_served += add_numbers # add_numbers是一个方法参数
        print(f'餐馆每天可接待的就餐人数为：{self.number_served}')

# 创建Restaurant实例
r1 = Restaurant('h海碗居','面食')
r1.describe_restaurant()
r1.open_restaurant()
r1.set_number_served(100) # # 修改实例变量 number_served 的值
r1.increment_number_served(50) # 传递50到add_numbers中

