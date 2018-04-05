# _*_ coding: utf-8 _*_
"""
  Created by bidoli on 2018/4/2.
"""
from flask import Blueprint

__author__ = 'Alimazing'

web = Blueprint('web', __name__)

from app.web import book
from app.web import user