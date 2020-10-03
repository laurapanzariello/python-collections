class CheckingAccount():
	
	def __init__(self, account):
		self.account = account
		self.balance = 0

	def deposit(self, value):
		self.balance += value

	def __str__(self):
		return "[>> Account {} Balance {}<<]".format(self.account, self.balance)


if __name__ == '__main__':
	code = input("Account number: ")
	new = CheckingAccount(code)
	print(new)
