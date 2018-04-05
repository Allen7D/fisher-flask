# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
from . import web

__author__ = 'Alimazing'

@web.route('/user/search/<id>')
def search_id(id):
	return 'temporary info'