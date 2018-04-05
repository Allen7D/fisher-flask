# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/3.
"""
__author__ = 'Alimazing'

class BookViewModel():
	@classmethod
	def package_singel(cls, data, keyword):
		returned = {
			'books': [],
			'total': 0,
			'keyword': keyword
		}
		if data:
			returned['total'] = 1
			returned['books'] = [cls.__cut_book_data(data)]
		return returned

	@classmethod
	def package_collection(cls, data, keyword):
		returned = {
			'books': [],
			'total': 0,
			'keyword': keyword
		}
		if data:
			returned['total'] = data['total']
			returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
		return returned

	@staticmethod
	def __cut_book_data(data):
		book = {
			'title': data['title'],
			'publisher': data['publisher'],
			'author': '、'.join(data['author']),
			'pages': data['pages'] or '',
			'price': data['price'],
			'summary': data['summary'] or 'z',
			'image': data['image']
		}
		return book