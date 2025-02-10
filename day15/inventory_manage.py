"""
实战思路
查询商品库存：从文件中读取商品库存数据并展示。
修改商品库存：根据商品名称修改库存数量。
添加新商品：向文件中添加新的商品记录。

捕获用户输入错误（如输入非数字时的类型异常）。
捕获文件读写错误。
捕获商品名称不存在的自定义异常。
"""

import sys

# 读取文件
def read_inventory(filename):
    try:
        with open(filename,'r',encoding='utf-8') as file:
            # 初始化库存
            inventory = {}
            inventory_data = file.readlines()

            for line in inventory_data:
                product_name,amount = line.strip().split(',')
                inventory[product_name] = float(amount)
            return inventory
    except FileNotFoundError:
        print('文件不存在，创建新文件')
        with open(filename, 'w', encoding='utf-8') as file:
            pass
        return {}
    except Exception as e:
        print('读取文件发生错误：',e)
# 写入文件
def write_inventory(filename,inventory):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for product_name,amount in inventory.items():
                file.write(f'{product_name},{amount}\n')
    except Exception as e:
        print(f'写入文件发生错误：{e}')
# 查询商品库存
def query_inventory(inventory):
    if not inventory:
        print('商品库存系统为空')
    else:
        print('展示商品库存信息：')
        for product_name,amount in inventory.items():
            print(f'商品{product_name},库存{amount}件')
#修改商品库存
def modify_inventory(inventory,product_name,new_amount):
    try:
        if product_name not in inventory:
            print('商品名称不存在！！')
        else:
            inventory[product_name] = new_amount
            print(f'商品{product_name},库存修改为{new_amount}件')
    except Exception as e:
        print(f'修改商品库存时发生错误：{e}')
# 添加新商品
def add_inventory(inventory,product_name,amount):
    if product_name in inventory:
        print('商品名称已存在')
    else:
        inventory[product_name] = amount
        print(f'商品{product_name},库存数量{amount}添加成功哦')
# 主程序
def inventory_manage():
    filename = 'inventory.txt'
    inventory = read_inventory(filename)
    # print('-'*20)
    print('-'*20,'欢迎进入商品库存管理系统！！！','-'*20)
    while True:
        print("————————————————————————————————————————")
        print('请选择下列操作：\n'
              '1.查询库存\n'
              '2.修改库存\n'
              '3.添加新商品\n'
              '4.退出系统')
        try:
            choice = int(input('请输入操作编号：'))
        except ValueError:
            print('输入的操作编号不存在，请重新输入')
        else:
            if choice == 1:
                query_inventory(inventory)
            elif choice == 2:
                try:
                    product_name = input('请输入商品名称：').capitalize().strip()
                    new_amount= float(input('请输入要修改库存数量：'))
                    write_inventory(filename, inventory)
                    modify_inventory(inventory,product_name,new_amount)
                except Exception as e:
                    print('库存数量应为数字。。。。。。',f'\n报错信息：{e}')
            elif choice == 3:
                try:
                    product_name = input('请输入商品名称：').capitalize().strip()
                    amount = float(input('请输入库存数量：'))
                    write_inventory(filename, inventory)
                    add_inventory(inventory,product_name,amount)
                except ValueError as e:
                    print('库存数量应为数字。。。。。。',f'\n报错信息：{e}')
            elif choice == 4:
                # print('已退出当前系统！！！\n')
                print('-'*20,'已退出当前系统!','-'*35)
                sys.exit()
            else:
                print('输入的操作编号不存在，请重新输入')



if __name__ == '__main__':
    inventory_manage()

