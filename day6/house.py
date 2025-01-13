"""
实战代码
房子有户型，总面积和家具名称列表，新房子没有任何的家具。
家具有名字和占地面积，其中
床：占 4 平米
衣柜：占 2 平米
餐桌：占 1.5 平米
将以上三件家具添加到房子中
打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""
# 定义房子类
class House:
    # 定义房子的实例属性 户型、总面积、家具名称列表
    def __init__(self, house_type, total_area):
        '''
        :param house_type: 房屋户型
        :param total_area: 房屋总面积
        '''
        self.house_type = house_type
        self.total_area = total_area
        self.useful_area = total_area #剩余面积
        self.furniture_list = [] #furniture 家具对于房子来说家具名称都一样

    # 将家具添加到房子中
    def add_furniture(self, furniture):
        '''
        添加家具
        :param furniture: 家具对象
        :return:
        '''
        # 判断家具的占地面积是否超过剩余面积
        if self.useful_area >= furniture.area:
            # 将家具对象添加到家具列表中
            self.furniture_list.append(furniture)
            # 更新剩余面积
            self.useful_area -= furniture.area
            print(f'{furniture.name}已经添加到房子中，剩余可用面积为：{self.useful_area}')
        else:
            print(f'\n房屋可用面积不足，无法添加家具～～～')

    # 输出房子的户型，总面积，剩余面积，家具名称列表
    def display_info(self):
        print('\n房子的信息为：')
        print(f'户型：{self.house_type}')
        print(f'总面积：{self.total_area}')
        print(f'剩余面积：{self.useful_area}')

        print('\n家具名称列表：')
        for f in self.furniture_list:
            print(f.name)

# 定义家具类
class Furniture:
    # 定义家具的实例属性 名字、占地面积
    def __init__(self, name, area):
        '''
        名字和占地面积
        :param name: 家具名称
        :param area: 家具占地面积
        '''
        self.name = name
        self.area = area
    def __str__(self):
        return f'家具名称{self.name},占地面积{self.area}'

# 创建房子的对象 实例化房子的类
my_house = House('三室一厅', 120)

# 创建家具的对象 实例化家具的类
bed = Furniture('床', 4)
wardrobe = Furniture('衣柜', 2)
table =Furniture('餐桌', 1.5)

# 添加家具到房子中 通过房子的对象调用add_furniture方法
my_house.add_furniture(bed)
my_house.add_furniture(wardrobe)
my_house.add_furniture(table)

# 打印房子的信息
my_house.display_info()



