
# -----------------1-----------------

class Account():

    def __init__(self,username,password,balance=0):

        assert len(password) >= 8, "Password must be at least 8 symbols"

        self.username = username
        self.__password = password
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount

        return print(f'Deposit of {amount} $ has been accepted')

    def withdraw(self,amount):
        if amount > self.balance:
            print("You don't have enough money on deposit")
        else:
            self.balance = self.balance - amount
            return print(f'Withdrawal of {amount} $ has been accepted')

    def send(self,amount,account):

        self.account = account

        if amount > self.balance:
            print("You don't have enough money on deposit")
        else:
            self.balance = self.balance - amount
            return print(f'{amount} $ has been sent to {self.account}')

    def __repr__(self):
        return f'Account Balance: {self.balance}'

my_balance = Account('Vakho', '12345678', 100)

my_balance.withdraw(50)
print(my_balance)

my_balance.deposit(200)
print(my_balance)

my_balance.send(15,"GE129TBC993 2233 33 32423")
print(my_balance)

