from oo.bank import Account


class CheckingAccount(Account):

    def tax(self):
        self._balance -= 2


class SavingsAccount(Account):

    def tax(self):
        self._balance *= 1.01
        self._balance -= 3


if __name__ == '__main__':
    code = input("CheckingAccount number: ")
    check = CheckingAccount(code)
    check.deposit(1000)
    print(check)
    code = input("SavingsAccount number: ")
    save = SavingsAccount(code)
    save.deposit(1000)
    print(save)

    for c in [check, save]:
        c.tax()
        print(c)
