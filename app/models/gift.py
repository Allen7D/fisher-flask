# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/10.
"""
from flask import current_app
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook

__author__ = 'Alimazing'


class Gift(Base):
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False) # 可以不唯一(可多次被拥有)
	# book = relationship('Book')
	# bid = Column(Integer, ForeignKey('book.id'))
	launched = Column(Boolean, default=False)

	@classmethod
	def get_user_gifts(cls, uid):
		gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
			desc(Gift.create_time)).all()
		return gifts

	@classmethod
	def get_wish_counts(cls, isbn_list):
		from app.models.wish import Wish
		count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
			Wish.launched == False,
			Wish.isbn.in_(isbn_list),
			Wish.status == 1).group_by(
			Wish.isbn).all()
		return [{'count': wish[0],'isbn': wish[1]} for wish in count_list]

	@property
	def book(self):
		yushu_book = YuShuBook()
		yushu_book.search_by_isbn(self.isbn)
		return yushu_book.first


	@classmethod
	def recent(cls):
		recent_gifts = Gift.query.filter_by(
			launched=False).group_by(
			Gift.isbn).order_by(
			desc(Gift.create_time)).limit(
			current_app.config['RECENT_BOOK_COUNT']).distinct().all()
		return recent_gifts