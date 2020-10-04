from abc import ABCMeta
from abc import abstractmethod


class Account(metaclass=ABCMeta):
	
	def __init__(self, account):
		self._account = account
		self._balance = 0

	def deposit(self, value):
		self._balance += value

	def __str__(self):
		return "[>> Account {} Balance {}<<]".format(self._account, self._balance)

	@abstractmethod
	def tax(self):
		pass
