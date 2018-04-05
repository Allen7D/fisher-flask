# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel
from . import web

__author__ = 'Alimazing'


@web.route('/book/search')
def search():
	form = SearchForm(request.args) # validator层(参数校验)
	if form.validate():
		q = form.q.data.strip()
		page = form.page.data
		isbn_or_key = is_isbn_or_key(q)
		if isbn_or_key == 'isbn':
			result = YuShuBook.search_by_isbn(q) # 请求(数据获取)
			result = BookViewModel.package_singel(result, q) # viewModel层(数据加工)
		else:
			result = YuShuBook.search_by_keyword(q, page)
			result = BookViewModel.package_collection(result, q)
		return jsonify(result)
	else:
		return jsonify(form.errors)

