# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/10.
"""
from . import web

__author__ = 'Alimazing'


@web.route('/')
def index():
    return 'Hello, fisher'


@web.route('/personal')
def personal_center():
    pass
