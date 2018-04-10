# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/10.
"""
from . import web
from flask_login import login_required


__author__ = 'Alimazing'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



