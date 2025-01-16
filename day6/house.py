"""
实战代码
房子有户型，总面积和家具名称列表，新房子没有任何的家具。

家具有名字和占地面积，

床：占 4 平米
衣柜：占 2 平米
餐桌：占 1.5 平米
将以上三件家具添加到房子中
打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""
# 定义房子类
class House:
    def __init__(self,house_type,total_area):
        """
        # 构造方法，初始化房子户型、房子总面积、家具名称列表
        :param house_type: 房子户型
        :param total_area: 房子总面积
        :param furniture_list: 家具名称列表
        """
        self.house_type = house_type
        self.total_area = total_area
        self.furniture_lst = []
        self.userful_area = total_area

    def add_furniture(self,furniture):
        """
        # 添加家具
        :return:
        """
        # 判断总面积是否大于家具面积
        if self.total_area > furniture.area:
            # 可将家具添加到房子中
            self.furniture_lst.append(furniture)
            print(f'{furniture.name}添加成功')
            # 输出剩余面积信息
            self.userful_area = self.total_area -furniture.area
        else:
            # 面积不足，无法添加家具
            print('剩余面积不足，无法添加家具')


    def show_info(self):
        """
        # 打印房子信息
        :return:
        """
        # 输出房子户型信息
        print(f'房子户型信息为：{self.house_type}')
        # 输出房子总面积信息
        print(f'房子总面积信息为：{self.total_area}')
        # 输出房子剩余面积信息
        print(f'房子的剩余面积为：{self.userful_area}\n')
        # 输出家具名称列表
        for furniture in self.furniture_lst:
            print(f'家具名称为：{furniture}')

# 定义家具类
class Furniture:
    def __init__(self,name,area):
        """
        #  构造方法，初始化家具名称和占地面积
        :param name: 家具名称
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area
    def __str__(self):
        """
        # 返回家具信息
        :return:
        """
        return f'{self.name}的占地面积为{self.area}平方米'

# 创建房子的实例对象
my_house = House('四室两厅',130)

# 创建家具的实例对象
bed = Furniture('床',4)
wardrobe= Furniture('衣柜',2)
table = Furniture('餐桌', 1.5)

# 调用add_furniture方法，将家具添加到房子中
my_house.add_furniture(bed)
my_house.add_furniture(wardrobe)
my_house.add_furniture(table)

# 显示房子信息
my_house.show_info()