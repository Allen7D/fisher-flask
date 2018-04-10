# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/10.
"""
from flask import request, jsonify
import json

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from . import api

__author__ = 'Alimazing'


@api.route('/api/book')
def search():
	form = SearchForm(request.args) # validator层(参数校验)
	books = BookCollection()

	if form.validate():
		q = form.q.data.strip()
		page = form.page.data
		isbn_or_key = is_isbn_or_key(q)
		yushu_book = YuShuBook()

		if isbn_or_key == 'isbn':
			yushu_book.search_by_isbn(q)
		else:
			yushu_book.search_by_keyword(q, page)

		books.fill(yushu_book, q)
		return json.dumps(books, default=lambda o: o.__dict__)
	else:
		return jsonify(form.errors)
