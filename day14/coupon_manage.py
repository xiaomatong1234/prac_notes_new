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


def read_coupon_file(filename):
    try:
        with open(filename, 'r') as file:
            # 初始化优惠券列表
            coupon_lst  = []
            # 读取 JSON 文件
            data = json.load(file)
            for line in data:
                product_name,discount = line.strip().split(',')
                coupon_lst[product_name] = float(discount)
            return coupon_lst
    except FileNotFoundError:
        print('文件不存在，新创建一个文件')
        with open(filename, 'w', encoding='utf-8') as file:
            pass
        return {}
    except ValueError:
        print('请检查文件格式是否正确！')
        return {}
def write_coupon_file(filename:str, coupon_lst: Dict[str, int]):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(coupon_lst, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'写入文件时出错{e}')
def query_coupon(filename):
    """选择查看当前优惠"""
    pass
def update_coupon(filename):
    """申请新的优惠券"""
    pass
def add_coupon(filename,product_name,discount):
    """添加优惠"""
    pass
def del_coupon(filename):
    """删除过期或错误的优惠信息"""
    pass
def coupon_manage():
    filename = 'coupon.json'
    coupon_lst = read_coupon_file(filename)
    while True:
        print('请选择下列操作：\n'
              '1.查询当前优惠\n'
              '2.更改新的优惠\n'
              '3.添加优惠信息\n'
              '4.删除优惠信息\n'
              '5.退出系统')
        try:
            choice = int(input('请输入操作编号：'))
            if choice == 1:
                query_coupon(filename)
            elif choice == 2:
                update_coupon(filename)
                write_coupon_file(filename, coupon_lst)
            elif choice == 3:
                product_name = input('请输入商品名称：')
                discount = random.randint(1,10)
                add_coupon(filename,product_name,discount)
                write_coupon_file(filename, coupon_lst)
            elif choice == 4:
                del_coupon(filename)
                write_coupon_file(filename, coupon_lst)
            else:
                print('已退出当前系统！！')
                write_coupon_file(filename, coupon_lst)
                break
        except ValueError:
            print('请输入正整数！！！')


if __name__ == '__main__':
    coupon_manage()