class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, value):
        self.balance += value
    
    def withdraw(self, value):
        self.balance -= value

    def add_interest(self):
        self.balance += self.balance / 100 * self.interest_rate
    


account = BankAccount(200, 12)
account.deposit(200)
print(f'После пополнения счета, баланс состовляет: ',account.balance)
account.withdraw(20)
print(f'После списания суммы со счета, баланс состовляет: ',account.balance)
account.add_interest()
print(f'После добавления процентов к сумме счета, баланс состовляет: ',account.balance)