class Book:
	def __init__(self, year):
		if str(year) == '2020':
			self.book = 'balabala'
		else:
			self.book = 'wakao'

	def book_name(self):
		return self.book
