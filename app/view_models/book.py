# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/3.
"""
__author__ = 'Alimazing'

class BookViewModel:
	def __init__(self, book):
		self.title = book['title']
		self.publisher = book['publisher']
		self.author = '、'.join(book['author'])
		self.image = book['image']
		self.price = book['price']
		self.summary = book['summary']
		self.pages = book['pages']


class BookCollection:
	def __init__(self):
		self.total = []
		self.books = []
		self.keyword = ''

	def fill(self, yushu_book, keyword):
		self.total = yushu_book.total
		self.keyword = keyword
		self.books = [BookViewModel(book) for book in yushu_book.books]