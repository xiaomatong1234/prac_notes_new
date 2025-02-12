"""销售数据管理与分析"""
import copy

# 商品列表
product_lst = []

# 添加销售记录
"""
用户输入信息：输入产品名称、销售数量、单价
使用字典管理单个商品信息
把单个商品的字典添加到商品列表中
"""
def add_sales(product_names, quantities, prices):
    # 单个商品信息
    product_info = {
        "product_names": product_names,
        "quantities": quantities,
        "prices": prices
    }

    product_lst.append(product_info)
    return product_lst

# 用户输入销售产品信息
product_name = input('请输入产品名称：')
quantity =  float(input('请输入产品数量：'))
price =  float(input('请输入产品价格：'))
add_product_msg = add_sales(product_name, quantity, price)
print('展示商品列表：',add_product_msg)

# 更新销售记录
"""
输入产品名称
在商品列表中查找商品记录，输入新销售数量，输入新单价，修改商品信息
"""
def update_sales(product_names, new_quantities, new_prices):
    for product in product_lst:
        if product["product_names"] == product_names:
            product["quantities"] = new_quantities
            product["prices"] = new_prices
            return f'商品 {product_names} 更新成功！'
    return '该产品不在商品列表中！！'

# 用户输入更新销售记录
product_name = input('请输入产品名称：')
quantity =  float(input('请输入更新后的产品数量：'))
price =  float(input('请输入更新后产品价格：'))

update_product_msg = update_sales(product_name, quantity, price)
print('展示更新后的商品列表：',update_product_msg)

# 删除销售记录
"""
输入产品名称
在商品列表中查找商品记录，删除商品
"""
def del_sales(product_names):
    for product in product_lst:
        if product["product_names"] == product_names:
            product_lst.remove(product)
            return f'商品 {product_names} 删除成功！'
    return "商品不存在"

product_name = input('请输入要删除的产品名称：')
del_product_msg = del_sales(product_name)
print(del_product_msg)
print(f'展示当前商品列表：{product_lst}')

# 统计销售数据
"""
计算销售总额
展示商品信息列表
"""
def total_sales():
    total_amounts = 0
    if product_lst:
        for product in product_lst:
            total_amounts += product["quantities"] * product["prices"]
            return total_amounts
    return "商品列表不存在"

total_sales()
print('总销售额为：',total_sales())
print(f'系统中的全部商品信息为{product_lst}')

# 备份销售数据
def deep_copy_sales():
    copy_sales = copy.deepcopy(product_lst)
    return copy_sales

print('展示已备份的销售数据：',deep_copy_sales())

# 恢复销售数据
def recover_sales():
    pass

# 修改备份数据
"""
输入备份数据修改信息
查看浅拷贝与深拷贝的区别
"""
def change_sales():
    pass

# 销售数据管理系统