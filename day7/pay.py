# 创建基础类
class Payment:
    def pay(self,nums):
        """
        支付方法
        :return:
        """
        pass

# 创建CreditCardPayment子类
class CreditCardPayment(Payment):
    def pay(self,nums):
        """
        信用卡支付
        :return:
        """
        print(f"当前支付方式是信用卡支付：{nums}元")

# 创建PayPalPayment子类
class PayPalPayment(Payment):
    def pay(self,nums):
        """
        支付宝支付
        :return:
        """
        print(f"当前支付方式是支付宝支付：{nums}元")

# 多肽状态下使用相同的对象名，调用相同的方法，传入数据实现不同的行为
def use_pay(payment, nums):
    """
    w完成支付方法
    :param payment:支付对象
    :param nums: 支付金额
    :return:
    """
    payment.pay(nums)
# 创建支付对象
cp = CreditCardPayment()
pp = PayPalPayment()

# 使用信用卡支付
use_pay(cp, 12)
# 使用支付宝支付
use_pay(pp, 23)

# # 创建实例化对象
# c = CreditCardPayment()
# p = PayPalPayment()
#
# # 调用方法
# c.pay(12)
# p.pay(23)