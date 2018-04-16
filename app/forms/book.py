# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, ValidationError

from app.libs.helper import is_isbn_or_key

__author__ = 'Alimazing'

class SearchForm(Form):
	q = StringField(validators=[DataRequired(), Length(min=1,  max=30)])
	page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)