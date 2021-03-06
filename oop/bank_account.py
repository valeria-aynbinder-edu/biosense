# Class has state represented by attributes, and the state
# is changed using class methods
from oop.person import Person


class BankAccount:

    def __init__(self, account_num: int, account_owner: Person, limit=10000):
        print(f"Caaling __init__")
        self.account_num = account_num
        self.owner: Person = account_owner
        self.limit = limit

        self.balance = 0

    def deposit(self, amount):
        print(f"Caaling deposit")
        self.balance += amount
        print(f"Your new balance is {self.balance}")

    def withdraw(self, amount):
        print(f"Caaling withdraw")
        if self.balance - amount < -self.limit:
            print(f"Sorry, you cannot withdraw, your balance is: {self.balance}")
        else:
            self.balance -= amount
            print(f"Your new balance is {self.balance}")


if __name__ == '__main__':

    person1 = Person('Moshe', 'Israeli', 'Tel-Aviv', 'Rotshild 45', '0545555555', 'moshe@gmail.com', 28)
    account1 = BankAccount(12345, person1)

    account1.deposit(100)
    account1.withdraw(10000)
    account1.withdraw(1000)