"""
实战：银行账户系统
设计一个银行账户系统 BankAccount 类，支持以下基本功能
存款 (deposit)：向账户中存入指定金额。
取款 (withdraw)：从账户中提取指定金额，且取款金额不能超过账户余额。
获取余额 (get_balance)：获取当前账户的余额。
转账 (transfer)：从当前账户向另一个账户转账，转账金额不能超过账户余额。
使用 Pytest 测试框架进行单元测试
测试存款、取款、获取余额、转账方法的正确性。
配置测试环境的初始化和清理。
"""
from day16.src.bank_account import BankAccount


class TestBankAccount:
    def setup_class(self):
        # 初始余额50
        self.bank_account = BankAccount(50)
    # 存款50
    def test_deposit(self):
        self.bank_account.deposit(50)
        assert self.bank_account.get_balance() == 100
    # 取款50
    def test_withdraw(self):
        self.bank_account.withdraw(50)
        assert self.bank_account.get_balance() == 0
    # 测试转账50
    def test_transfer(self):
        target_account = BankAccount(50)
        self.bank_account.transfer(50,target_account)
        assert self.bank_account.get_balance() == 0