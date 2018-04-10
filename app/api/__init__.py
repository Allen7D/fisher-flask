# _*_ coding: utf-8 _*_
"""
  Created by bidoli on 2018/4/10.
"""
from flask import Blueprint

__author__ = 'Alimazing'

api = Blueprint('api', __name__)

from app.api import book
