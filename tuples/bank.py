class Account:
	
	def __init__(self, account):
		self._account = account
		self._balance = 0

	def deposit(self, value):
		self._balance += value

	def __str__(self):
		return "[>> Account {} Balance {}<<]".format(self._account, self._balance)


if __name__ == '__main__':
	code = input("Account number: ")
	new = Account(code)
	print(new)
