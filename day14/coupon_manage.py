"""
随机商品优惠生成器
- 模拟一个电商平台的优惠活动系统。通过随机生成优惠券，为不同的商品设置折扣。

用户可以选择查看当前优惠、申请新的优惠券、以及删除过期或错误的优惠信息。

系统需要保证健壮性，处理用户输入和数据操作中的异常。
    - 装饰器：记录系统运行的日志，包括方法的调用时间和参数。
    - 异常处理：处理用户输入错误、字典键值不存在等情况。
    - random模块：随机生成优惠券的折扣值。
    -循环：实现用户交互的循环操作。
    - 判断：对用户输入进行判断。
    - 字符串：格式化输出优惠信息。
    - 列表：存储所有商品的优惠信息。
    - 字典：用于记录商品与对应的优惠。
"""
import json
import random
from typing import Dict

def log():
    pass
def read_coupon_file(filename):
    try:
        with open(filename, 'r') as file:
            # 初始化优惠券列表
            coupons  = {}
            # 读取 JSON 文件
            coupons_data = json.load(file)

            return coupons_data
    except FileNotFoundError:
        print('文件不存在，新创建一个文件')
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
        return {}
    except json.JSONDecodeError:
        print('请检查文件格式是否正确！')
        return {}
def write_coupon_file(filename, coupons):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(coupons, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'写入文件时出错{e}')
def query_coupon(coupons):
    """选择查看当前优惠"""
    if not coupons:
        print('商品优惠管理内容为空\n')
    else:
        for product_name, discount in coupons.items():
            print(f'商品{product_name}:{discount}%折扣')
def update_coupon(filename,coupons,product_name,new_discount):
    """申请新的优惠券"""
    if product_name in coupons:
        coupons[product_name] = new_discount
        write_coupon_file(filename, coupons)
        print(f'更新商品{product_name}:{new_discount}%折扣\n')
    else:
        print(f'商品{product_name}不存在\n')
def add_coupon(filename,coupons,product_name,discount):
    """添加优惠"""
    if product_name in coupons:
        print(f'商品{product_name}已存在，请重新输入！！！\n')
    else:
        coupons[product_name] = discount
        write_coupon_file(filename, coupons)
        print(f'-商品{product_name}:{discount}%折扣,添加成功！！！')
def del_coupon(coupons):
    """删除过期或错误的优惠信息"""
    pass

def coupon_manage():
    filename = 'coupon.json'
    coupons = read_coupon_file(filename)
    while True:
        print('\n请选择下列操作：\n'
              '1.查询当前优惠\n'
              '2.更改新的优惠\n'
              '3.添加优惠信息\n'
              '4.删除优惠信息\n'
              '5.退出系统')
        try:
            choice = int(input('请输入操作编号：'))
            if choice == 1:
                query_coupon(coupons)
            elif choice == 2:
                product_name = input('请输入商品名称：')
                new_discount = random.randint(1,90)
                update_coupon(filename,coupons,product_name,new_discount)

            elif choice == 3:
                product_name = input('请输入商品名称：')
                discount = random.randint(1,90)
                add_coupon(filename,coupons,product_name,discount)

            elif choice == 4:
                del_coupon(coupons)
                write_coupon_file(filename, coupons)
            else:
                print('已退出当前系统！！')
                write_coupon_file(filename, coupons)
                break
        except ValueError:
            print('请输入正整数！！！\n')


if __name__ == '__main__':
    coupon_manage()