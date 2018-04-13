# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
from flask import request, render_template, flash
from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
from . import web

__author__ = 'Alimazing'


@web.route('/book/search')
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
	else:
		flash('搜索的关键字不符合要求，请重新输入关键字')
	return render_template('search_result.html', books=books, form=form)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
	has_in_gifts = False
	has_in_wishes = False

	# 取书籍详情数据
	yushu_book = YuShuBook()
	yushu_book.search_by_isbn(isbn)
	book = BookViewModel(yushu_book.first)

	if current_user.is_authenticated:
		has_in_gifts, has_in_wishes = current_user.has_in_list(isbn)

	trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
	trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

	trade_gifts_model = TradeInfo(trade_gifts)
	trade_wishes_model = TradeInfo(trade_wishes)

	return render_template('book_detail.html',
	                       book=book,
	                       gifts=trade_gifts_model, wishes=trade_wishes_model,
	                       has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)
