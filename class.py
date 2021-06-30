#!/usr/bin/env python


class Calculator:

	def __init__(self, ina, inb):
		self.a = ina
		self.b = inb


	def add(self):
		return self.a + self.b

	def multiply(self):
		return self.a*self.b


#scientific CAlculator

class Scientific(Calculator):

	def power(self):
		return pow(self.a, self.b)


def quickadd(a, b):
	return a+b
