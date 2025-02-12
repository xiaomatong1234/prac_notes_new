import pytest
from day16.src.shop import Product, ShoppingCart
def setup_module():
    print('\n【开始测试】\n')
def teardown_module():
    print('\n【结束测试】\n')

class TestShopCart:
    def setup_class(self):
        # # 实例化商品
        # self.product = Product('apple', 100)
        # 实例化购物车
        self.cart = ShoppingCart()
    def setup_method(self):
        # 清空购物车
        print('测试前数据准备：')
        self.cart.clear_cart()
    @pytest.mark.parametrize(
        "product",
        [
        Product("apple",100),
        Product("orange",200),
        Product("cherry",300)
        ],
        ids=[
            "add_apple","add_orange","add_cherry"
        ]
    )
    ## 正向测试流程
    # 测试用例：商品添加到购物车
    def test_add_product(self,product):
        # 添加商品购物车
        self.cart.add_product(product)
        # 断言商品添加到购物车
        assert product in self.cart.product_lst
        assert len(self.cart.product_lst) == 1
    @pytest.mark.parametrize(
        "product",
        [
            Product("apple", 100),
            Product("orange", 200),
            Product("cherry", 300)
        ],
        ids=['remove_apple', 'remove_orange', 'remove_cherry']

    )
    # 测试用例：购物车移除商品
    def test_remove_product(self,product):
        self.cart.add_product(product)
        # 从购物车移除商品
        self.cart.remove_product(product)
        assert product not in self.cart.product_lst
        assert len(self.cart.product_lst) == 0
        assert self.cart.calculate_total() == 0
    @pytest.mark.parametrize(
        "product,product1,product2",
        [
            (Product("apple", 100),Product("orange", 200),Product("cherry", 300))
        ],
        ids=['cal_apple_100:orange_200:cherry_300']
    )
    # 测试用例：计算购物车中商品总价
    def test_calculate_total(self,product,product1,product2):
        self.cart.add_product(product)
        self.cart.add_product(product1)
        self.cart.add_product(product2)
        assert self.cart.calculate_total() == 600
    # 测试用例：清空购物车
    def test_clear_cart(self):
        result = self.cart.product_lst.clear()
        assert result is None


    # 逆向测试流程