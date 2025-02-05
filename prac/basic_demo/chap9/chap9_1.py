# 创建Restaurant类
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        """
        初始化实例属性
        :param restaurant_name: 饭店名称
        :param cuisine_type:菜系
        """
        self.restaurant_name= restaurant_name.title()
        self.cuisine_type = cuisine_type
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


# 创建Restaurant实例
r1 = Restaurant('h海碗居','面食')
r1.describe_restaurant()
r1.open_restaurant()