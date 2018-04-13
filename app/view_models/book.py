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
		self.isbn = book['isbn']
		self.pages = book['pages']
		self.pubdate = book['pubdate']
		self.binding = book['binding']

	@property
	def intro(self):
		intros = filter(lambda x: True if x else False,
		                [self.author, self.publisher, self.price])
		return ' / '.join(intros)

class BookCollection:
	def __init__(self):
		self.total = []
		self.books = []
		self.keyword = ''

	def fill(self, yushu_book, keyword):
		self.total = yushu_book.total
		self.keyword = keyword
		self.books = [BookViewModel(book) for book in yushu_book.books]
