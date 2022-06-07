# Class has state represented by attributes, and the state
# is changed using class methods
from oop.person import Person


class BankAccount:

    def __init__(self, account_num: int, account_owner: Person, limit=10000):
        self.account_num = account_num
        self.owner: Person = account_owner
        self.limit = limit

        self.balance = 0