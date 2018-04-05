# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

__author__ = 'Alimazing'

db = SQLAlchemy()

class Book(db.Model):
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(50), nullable=False)
	author = Column(String(30), default='未名')
	binding = Column(String(20))
	publisher = Column(String(50))
	price = Column(String(20))
	pages = Column(Integer)
	pubdate = Column(String(20))
	isbn = Column(String(15), nullable=False, unique=True)
	summary = Column(String(1000))
	image = Column(String(50))