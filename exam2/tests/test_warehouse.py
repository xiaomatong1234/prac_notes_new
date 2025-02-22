"""测试目标：
编写 Pytest 测试用例，测试库存管理、订单管理和物流管理模块。

使用 Pytest 标记测试用例，组织测试顺序。

测试异常处理，包括库存不足和无效订单等情况。

使用 fixture 管理测试资源，模拟系统初始化。

使用 Pytest 配置文件配置全局选项。

使用 pytest.mark.parametrize 实现数据驱动，测试不同商品信息查询的场景。
"""
import pytest
import yaml

from exam2.src.warehouse_system import SmartSystem
def get_yaml():
    with open("../data/warehouse.yaml") as file:
        data = yaml.safe_load(file)
        print('data', data)
    return data


class TestWarehouse:
    def setup_class(self):
        self.smartsystem = SmartSystem()


    def test_stock_management(self):
        pass


    @pytest.mark.parametrize(
        "order_id,product,amount",
        [
            1001,(1,'apple',1,1),1
        ]
    )
    def test_order_management(self,order_id,product,amount):
        result = self.smartsystem.creat_order(order_id, product, amount)
        assert result == "创建订单成功"

    def test_logistics(self):
        pass
