import pytest

from day16.src.bank_account import BankAccount


class TestBankAccount:
    def setup_class(self):
        # 初始余额50
        self.bank_account = BankAccount(50)

    @pytest.mark.parametrize(
        "num,expected",
        [
            [50,100]
        ],
        ids = ["50,100"]
    )
    # 存款50
    def test_deposit(self, num, expected):
        self.bank_account.deposit(num)
        assert self.bank_account.get_balance() == expected

    @pytest.mark.parametrize(
        "num,expected",
        [
            [50,50]
        ]
    )
    # 取款50
    def test_withdraw(self, num, expected):
        self.bank_account.withdraw(num)
        assert self.bank_account.get_balance() == expected

    @pytest.mark.parametrize(
        "num,expected",
        [
            [50,0]
        ]
    )
    # 测试转账50
    def test_transfer(self,num,expected):
        target_account = BankAccount(num)
        self.bank_account.transfer(num,target_account)
        assert self.bank_account.get_balance() == expected