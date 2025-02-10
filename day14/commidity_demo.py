import json
import os
users = [
    {'role':'staff',"username":"ben","password":1234},
    {'role':'manager',"username":"admin","password":1234}]

def auth(role):
    """装饰器"""
    #  # 核实用户身份，仅用户角色为管理员时，可对商品库存系统进行查询、修改、添加新的商品记录，其它角色的用户，无上述权限
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_user = None
            for user in users:
                if user['username'] == kwargs.get("username"):
                    current_user = user
                    break
            if current_user and current_user['role']== role:
                return func(*args, **kwargs)
            else:
                if current_user:
                    print(f'当前用户{current_user["username"]}没有权限') #
                else:
                    print('当前用户在系统中不存在')
        return wrapper
    return decorator
@auth("manager")
def get_commodities(db_file,username):
    """查询商品库存"""
    # 打开文件 读取文件
    with open(db_file, "r", encoding="utf-8") as f:
        commodities = f.read()
        print(f'当前商品库存为：{commodities}')
@auth("manager")
def update_commodity(db_file,username):
    """修改商品库存"""
    # 1、检查文件是否为空或不存在
    if os.path.exists(db_file) and os.stat(db_file).st_size > 0:
        with open(db_file, "r", encoding="utf-8") as f:
            try:
                commodities = json.load(f)
            except json.decoder.JSONDecodeError:
                print('文件内容格式错误，无法加载商品数据！\n')

    # 2、获取用户输入的商品名称和新库存数量
    c_name = input('想修改库存的商品名称：')
    new_amount = int(input('修改商品数量：'))
    # 3、查找商品并修改库存
    found = False # 记录是否找到商品
    for product in commodities:
        if product["CommodityName"] == c_name:
            product["CommodityAmount"] = new_amount # 修改商品库存
            found = True
            print(f'当前{c_name}商品库存修改为：{new_amount}','\n')
            break # 找到商品后退出循环
    # 4、如果商品不存在，给出提示
    if not found:
        print("商品名称不存在在库存管理系统中！！\n")
        return  # 结束
    #5、更新json文件
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(commodities,f, ensure_ascii=False, indent=4)
        print('商品库存已修改！')
@auth("manager")
def add_commodity(db_file,username):
    """添加新商品"""
    c_name = input('商品名称：')
    amount = int(input('商品数量：'))
    price = float(input('商品价格：'))
    commodity_info = {
        "CommodityName":c_name,
        "CommodityAmount":amount,
        "CommodityPrice":price}
    #如果文件存在，读取文件内容，并向文件中追加新商品。
    # 如果文件存在且不为空则读取文件
    if os.path.exists(db_file) and os.stat(db_file).st_size > 0:
        with open(db_file, 'r', encoding='utf-8') as f:
            try:
                commodities= json.load(f)  # 读取JSON数组
            except json.decoder.JSONDecodeError:
                commodities = []  # 文件内容不合法，初始化数据
    # 文件不存在或为空，初始化为空列表
    else:
        commodities = []
     # 添加新商品
    commodities.append(commodity_info)

    # 重新写入json数据
    with open(db_file, 'w', encoding='utf-8') as f:
        file = json.dumps(commodities,ensure_ascii=False, indent=4)
        f.write(file)

    print('商品信息已添加\n')
def login():
    # 用户登陆
    # 给用户三次机会输入用户名、密码
    for count in range(3):
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if count < 3:
            for user in users:
                if user["username"] == username and user["password"] == int(password):
                    print('用户登陆成功！！')
                    return username
            print(f'用户名或密码输入错误，请重新输入！您还有{2 - count}次机会\n')
        count += 1
    print(f'3次机会已用完')
    return False
def run():
    # 商品库存文件
    db_file = 'orders.json'
    print("-"*40,'欢迎进入商品库存管理系统！！',"-"*40,'\n')
    print('【用户登陆页面】')
    # 用户登陆成功
    username = login()
    if username:
        while True:
            print('\n【商品库存管理系统目录】')
            print(
                '1、输入数字1，查询商品库存\n'
                '2、输入数字2，修改商品库存\n'
                '3、输入数字3，添加新商品\n'
                '4、输入数字4或其它数字，退出系统\n')
            num = int(input('请输入对应目录编号：'))
            try:
                if num == 1:
                    # 查询商品库存
                    get_commodities(db_file,username=username)
                elif num == 2:
                    # 修改商品库存
                    update_commodity(db_file,username=username)
                elif num == 3:
                    # 添加新商品
                    add_commodity(db_file,username=username)
                else:
                    try_again = input('请确认是否要退出商品库存管理系统？y/n：')
                    if try_again.lower() == 'y':
                        print("-" * 40, '已退出库存管理系统！', "-" * 46)
                        break
                    else:
                        # 循环继续
                        run()
            except ValueError:
                print("输入的操作编号必须是数字！")
    # 用户登陆失败
    else:
        print('登陆认证失败！')

if __name__ == '__main__':
    run()