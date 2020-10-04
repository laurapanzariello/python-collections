from tuples.bank import Account


class CheckingAccount(Account):

    def tax(self):
        self._balance -= 2


class SavingsAccount(Account):

    def tax(self):
        self._balance *= 1.01
        self._balance -= 3


if __name__ == '__main__':
    