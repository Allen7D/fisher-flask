# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/12.
"""
__author__ = 'Alimazing'

class BookCollection:
	def __init__(self):
		self.data = []
		self.cur = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.cur >= len(self.data):
			return StopIteration()
		r = self.data[self.cur]
		self.cur += 1
		return r

if __name__ == '__main__':
	books = BookCollection()
	books.data = ['《创世纪》', '《出埃及记》', '《利未记》', '《民数记》', '《申命记》']
	# for book in books:
	# 	print(book)

	print(next(books))
	print(next(books))
	print(next(books))