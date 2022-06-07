# Class has state represented by attributes, and the state
# is changed using class methods
from oop.person import Person


class Account:

    def __init__(self, account_num: int, limit=10000):
        print(f"Caaling __init__")
        self.account_num = account_num
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


class Person:

    def __init__(self, first_name, last_name, city, address, phone, email, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.address = address
        self.phone = phone
        self.email = email
        self.age = age
        self.accounts = []

    def is_using_gmail(self):
        return self.email.endswith("@gmail.com")

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts_num(self):
        return len(self.accounts)


if __name__ == '__main__':

    person1 = Person('Moshe', 'Israeli', 'Tel-Aviv', 'Rotshild 45', '0545555555', 'moshe@gmail.com', 28)
    account1 = Account(12345)
    account2 = Account(222222)

    person1.add_account(account1)
    person1.add_account(account2)

    print(person1.get_accounts_num())