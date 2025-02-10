"""
实战代码:
创建一个 Ecommerce 类，包含一个静态方法 calculate_discount。
静态方法接收商品的原价和折扣百分比，返回折扣后的价格。
实现如下功能：
使用静态方法计算不同商品的折扣价格。
在主程序中展示多个商品的折扣计算结果。
"""
class Ecommerce:

    @staticmethod
    def calculate_discount(price, discount):
        '''
        计算商品折扣后的价格
        :param price: 商品原价
        :param discount: 商品折扣 （0-100）
        :return: 折扣之后的价格
        '''
        if 0<=discount<=100:
            # 折扣后的价格
            discount_price =  price * (1-discount/100)
        else:
            print('折扣必须在0-100之间')
            discount_price = price
        return discount_price

# 商品列表
goods_list =[
    {'name':'手机','prices':100,'discount':12},
    {'name':'电脑','prices':500,'discount':10},
    {'name':'电视','prices':300,'discount':8},
    {'name':'冰箱','prices':200,'discount':6}
]
# 遍历商品列表，计算折扣后的价格
for good in goods_list:
    print(f'{good["name"]}的原价为：{good["prices"]}，折扣后的价格为：{Ecommerce.calculate_discount(good["prices"],good["discount"])}')



