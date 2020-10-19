from oo.account import CheckingAccount


class Account:

    def __init__(self, account):
        self._account = account
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return "[>> Account {} Balance {}<<]".format(self._account, self._balance)

    def __eq__(self, other):
        # check if the type of the account is the same
        if type(self) != type(other):
            return False
        return self._account == other._account

    def __lt__(self, other):
        if self._balance != other._balance:
            return self._balance < other._balance
        return self._account < other._account


if __name__ == '__main__':
    c1 = Account(1)
    c1.deposit(100)
    c2 = Account(1)
    c2.deposit(500)
    c3 = Account(4)
    c3.deposit(100)
    c4 = Account(3)
    c4.deposit(100)

    accounts = [c1, c2, c3, c4]
    for acc in accounts:
        print(acc)

    print("With the __lt__ method")

    for acc in sorted(accounts):
        print(acc)

    new_accounts = [c1, c3, c4]

    print("new list with just c1, c3 and c4")

    for acc in sorted(new_accounts):
        print(acc)
