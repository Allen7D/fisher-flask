# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/10.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

__author__ = 'Alimazing'

db = SQLAlchemy()

class Base(db.Model):
	__abstract__ = True
	status = Column(SmallInteger, default=1) # 软删除

	def set_attrs(self, attrs_dict):
		for key, value in attrs_dict.items():
			if hasattr(self, key) and key != 'id':
				setattr(self, key, value)
