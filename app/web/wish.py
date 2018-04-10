# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/10.
"""
from . import web

__author__ = 'Alimazing'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
