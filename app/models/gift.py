# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/10.
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = 'Alimazing'


class Gift(Base):
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False) # 可以不唯一(可多次被拥有)
	# book = relationship('Book')
	# bid = Column(Integer, ForeignKey('book.id'))
	launched = Column(Boolean, default=False)
