class BankError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

class BankAccount:
    
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, money):
        self.money = money
        try:
            if money <= 0 :
                raise BankError(str(money) + '원 입금불가')
        except BankError as e:
            print(e)
        else:
            self.balance += self.money
        finally:
            BankAccount.inquiry(self)

    def withdraw(self, money):
        self.money = money
        try:
            if money <= 0 :
                raise BankError(str(money) + '원 출금불가')
            if self.balance < money:
                raise BankError('잔액부족')
        except BankError as e:
            print(e)
        else:
            self.balance -= money
        finally:
            BankAccount.inquiry(self)
            

    def transfer(self, your_acc, money):
        self.your_acc = your_acc
        self.money = money
        try:
            if money > self.balance:
                raise BankError('잔액부족')
        except BacnkError as e:
            print(e)
        else:
            self.balance -= money
            your_acc.deposit(money)
        finally:
            BankAccount.inquiry(self)

    def inquiry(self):
        print(f'계좌번호: {self.acc_no}')
        print(f'통장 잔액: {self.balance}')

me = BankAccount('012-34-5678', 50000)
you = BankAccount('987-65-2312', 50000)

me.deposit(1000)
me.deposit(2000)
me.withdraw(1000)
me.transfer(you, 10000)
