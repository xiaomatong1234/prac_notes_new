"""
实战：商品库存管理系统
开发一个简单的商品库存管理系统，管理员可以查询商品的库存数量，修改库存值，并添加新的商品记录。
为了确保系统的稳定性，需要对输入异常、文件操作异常等进行处理，避免因用户输入错误或文件丢失导致系统崩溃。

查询商品库存：从文件中读取商品库存数据并展示。
修改商品库存：根据商品名称修改库存数量。
添加新商品：向文件中添加新的商品记录。
捕获用户输入错误（如输入非数字时的类型异常）。
捕获文件读写错误。
捕获商品名称不存在的自定义异常。
"""
class ProductNotFoundError(Exception):
    def __init__(self,message='商品未找到'):
        # 调用父类构造函数
        super().__init__(message)
        # 异常消息
        self.message = message
def read_inventory_file(filename):
    """
    打开文件
    解析文件内容并更新库存字典
    异常处理
    创建新文件(若文件不存在)
    :return:
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # 初始化库存信息
            inventory = {}
            file_content = file.readlines()
            for line in file_content:
                name,stock = line.strip().split(',')
                inventory[name] = int(stock)
            return inventory
    except FileNotFoundError:
        print('文件不存在，新创建一个文件')
        with open(filename, 'w', encoding='utf-8') as file:
            pass
        return {}
    except ValueError:
        print('请检查文件格式是否正确！')
        return {}
def write_inventory_file(filename, inventory):
    """
    打开文件
    写入库存字典
    异常处理
    :return:
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for name, stock in inventory.items():
                file.write(f'{name},{stock}\n')
    except Exception as e:
        print(f'写入文件时出错{e}')
def query_inventory(inventory):
    """
    查询库存 query_inventory
    :param inventory:
    :return:
    """
    if not inventory:
        print('商品库存为空\n')
    else:
        for name, stock in inventory.items():
            print(f'--{name}:{stock}件')
def update_inventory(inventory,name,new_stock):
    try:
        if name not in inventory:
            print(f'输入的{name}商品名称不存在！\n')
        else:
            # 更新商品库存
            inventory[name] = new_stock
            print(f'商品{name}库存已更新为{new_stock}件\n')
    except ProductNotFoundError as e:
        print(e)
def add_inventory(inventory,name,stock):
    if name in inventory:
        print('商品名称已存在，请务重复添加')
    else:
        inventory[name] = stock
        print(f'已添加商品{name}，库存{stock}件')
def inventory_management_system():
    """
    选择操作：
        查询库存 query_inventory
        修改库存 update_stock（检查商品是否存在、抛出ProductNotFoundError、更新库存字典）
        添加新商品 add_product
    检查商品是否存在
    添加新商品到字典
        退出系统（write_inventory_to_file）:打开文件、写入库存字典、异常处理
    :return:
    """
    filename = "inventory.txt"
    inventory = read_inventory_file(filename)
    while True:
        print('请选择下列操作\n'
              '1.查询库存\n'
              '2.修改库存\n'
              '3.添加新商品\n'
              '4.退出系统')
        try:
            choice = int(input('请输入操作编号：'))
            if choice == 1:
                query_inventory(inventory)
            elif choice == 2:
                name = input('请输入商品名称：')
                try:
                    new_stock = int(input('修改商品库存(件)：'))
                    update_inventory(inventory,name,new_stock)
                except ValueError:
                    print("输入无效！库存数量必须是正整数。")
            elif choice == 3:
                name = input('请输入商品名称：')
                try:
                    stock = int(input('请输入库存数量(件)：'))
                    add_inventory(inventory,name,stock)
                    write_inventory_file(filename, inventory)
                except ValueError:
                    print("输入无效！库存数量必须是正整数。")
            elif choice == 4:
                write_inventory_file(filename,inventory)
                print('已退出商品库存管理系统！！')
                break
        except ValueError:
            print("无效输入，请重新选择！\n")
if __name__ == '__main__':
    inventory_management_system()
