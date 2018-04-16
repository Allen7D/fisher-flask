# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/16.
  Created by Alimazing on 2018/4/16.
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, desc,func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook

__author__ = 'Alimazing'


class Wish(Base):
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False)
	launched = Column(Boolean, default=False)

	@classmethod
	def get_user_wishes(cls, uid):
		wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
			desc(Wish.create_time)).all()
		return wishes

	@classmethod
	def get_gift_counts(cls, isbn_list):
		from app.models.gift import Gift
		count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
			Gift.launched == False,
			Gift.isbn.in_(isbn_list),
			Gift.status == 1).group_by(
			Gift.isbn).all()
		return [{'count': gift[0],'isbn': gift[1]} for gift in count_list]

	@property
	def book(self):
		yushu_book = YuShuBook()
		yushu_book.search_by_isbn(self.isbn)
		return yushu_book.first