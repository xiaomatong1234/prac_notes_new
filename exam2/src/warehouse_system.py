# # 仓库管理系统
"""
智能仓库系统开发与测试:
你正在测试一个智能仓库系统。该系统可以管理库存、订单和物流。
你需要编写测试用例，确保系统功能正确，并能正确处理各种异常情况。

被测系统功能要求：

库存管理：每个商品有库存量，当商品库存为0时，用户无法下单。
订单管理：系统允许创建、查看、取消订单。
物流管理：每个订单会分配一个物流编号，物流状态可以是“待处理”、“运输中”、“已送达”。
商品信息查询：用户可以查询商品的名称、价格、库存等信息。

测试目标：
编写 Pytest 测试用例，测试库存管理、订单管理和物流管理模块。
使用 Pytest 标记测试用例，组织测试顺序。
测试异常处理，包括库存不足和无效订单等情况。
使用 fixture 管理测试资源，模拟系统初始化。
使用 Pytest 配置文件配置全局选项。
使用 pytest.mark.parametrize 实现数据驱动，测试不同商品信息查询的场景。
"""



class ProductManagement:
    """库存管理：商品有初始库存，商品库存为0，用户无法下单"""
    def __init__(self, good_id,name, price, stock):
        self.good_id = good_id
        self.name = name
        self.price = price
        self.stock = stock
    def show_product_info(self):
        print(f'展示产品信息：{self.good_id},{self.name},{self.price},{self.stock}')
        return f'展示产品信息：{self.good_id},{self.name},{self.price},{self.stock}'
class OrderManagement:
    def __init__(self,order_id,product,amount):
        self.order_id = order_id
        self.product = product
        self.amount = amount
    def get_order_info(self):
        return {
            "order_id": self.order_id,
            "product_name": self.product.name,
            "price": self.product.price,
            "amount": self.amount
        }
class SmartSystem:
    """订单管理：创建、查看、取消订单"""
    def __init__(self):
        self.orders = {}   # 订单编号：OrderManagement对象 属性 order_id,product,amount
        self.products = {} # 商品ID：ProductManagement对象 属性 good_id,name, price, stock
        self.logistics={}  # 订单编号：物流状态 order_id:status
    # 添加商品
    def add_product(self, product):
        self.products[product.good_id] = product # ProductManagement实例化对象
        return self.products
    # 创建订单
    def creat_order(self,order_id,product,amount):
        if order_id in self.orders:
            print('订单编号已存在')
            print('---------创建订单失败---------')
        elif product.good_id in self.products and product.stock >= amount:
            self.orders[order_id] = OrderManagement(order_id,product,amount)
            product.stock -= amount  # 减少库存
            self.logistics[order_id] = '待处理' # 初始化物流状态
            print(f'order_id:{order_id}，product_name:{product.name}，amount:{amount}订单添加成功！！')
            print('---------创建订单成功---------')
            return "创建订单成功"
            # return self.orders
        else:
            print('商品不存在或库存数量不足，无法下单')
            print('---------创建订单失败---------')
            return None
    def view_orders(self,order_id):
        if order_id in self.orders:
            order_info = self.orders[order_id]
            print(f'查询订单编号{order_id}：',order_info.get_order_info())
            return '查询订单成功'
        else:
            print('订单编号不存在')
            return '订单编号不存在'
    def cancel_order(self,order_id):
        if order_id in self.orders:
            order = self.orders[order_id]
            order.product.stock += order.amount  # 增加库存
            del self.orders[order_id] # 删除订单信息
            del self.logistics[order_id] # 删除物流信息
            print('订单已删除')
            return self.orders
        else:
            print('订单编号不存在')
            return None
    def update_logistics(self, order_id, status):
        if order_id in self.logistics:
            self.logistics[order_id] = status
            return f"订单 {order_id} 物流状态更新为: {status}"
        else:
            return "订单编号不存在"



# p = ProductManagement(21,'apple',1,1)
# p1 = ProductManagement(22,'orange',2,2)
#
# om = OrderManagement(11,p,1)
# om1 = OrderManagement(13,p,1)
# ss = SmartSystem()
# ss.add_product(p)
# ss.add_product(p1)
# ss.creat_order(11,p,1)
# ss.creat_order(11,p,1)
# ss.creat_order(13,p1,3)
# ss.view_orders(11)
# ss.view_orders(13)
# ss.cancel_order(11)
# ss.view_orders(11)



















