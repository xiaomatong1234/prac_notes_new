
class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print('存款金额为负数')
            return amount
        else:
            self.balance += amount
            return amount
    def withdraw(self, amount):
        if amount > self.balance:
            print('取款金额大于账户金额')
            return self.balance
        elif amount <= 0:
            print('取款金额必须大于0')
        else:
            self.balance -= amount
            return self.balance
    def get_balance(self):
        return self.balance
    def transfer(self, amount, target_account):
        if  amount > self.balance:
            print(f'当前账户余额{amount}不足')
            return self.balance
        elif amount < 0:
            print(f'转账金额{amount}不能为负数')
            return self.balance
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            return self.balance