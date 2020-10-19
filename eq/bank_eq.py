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


if __name__ == '__main__':
    c1 = Account(10)
    c2 = Account(10)
    c3 = CheckingAccount(10)

    print("With the __eq__ method")

    accounts = [c1]

    if c1 in accounts:
        print("c1 is in accounts")
    else:
        print("c1 is not in accounts")

    if c2 in accounts:
        print("c2 is in accounts")
    else:
        print("c2 is not in accounts")

    if c1 == c2:
        print("c1 == c2")
    else:
        print("c1 != c2")

    print("c3 is another type of account")
    if c1 == c3:
        print("c1 == c3")
    else:
        print("c1 != c3")
