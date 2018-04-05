# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
from app.libs.httper import HTTP
from flask import current_app
__author__ = 'Alimazing'

class YuShuBook:
	isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
	keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

	@classmethod
	def search_by_isbn(cls, isbn):
		url = cls.isbn_url.format(isbn)
		result = HTTP.get(url) # dict类型
		return result

	@classmethod
	def search_by_keyword(cls, keyword, page=1):
		url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
		result = HTTP.get(url)
		return result

	@staticmethod
	def calculate_start(page):
		return (page - 1) * current_app.config['PER_PAGE']