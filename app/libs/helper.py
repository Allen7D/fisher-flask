# _*_ coding: utf-8 _*_
"""
	Created by Alimazing on 2018/4/2.
"""
__author__ = 'Alimazing'


def is_isbn_or_key(word):
	"""
	判断 word 是 「isbn 还是 关键字」

	isbn:
	  isbn13 由13个0到9的数字组成
	  isbn10 由10个0到9的苏子组成，且含有一些 '-'
	"""
	isbn_or_key = 'key'
	if len(word) == 13 and word.isdigit():
		isbn_or_key = 'isbn'
	short_word = word.replace('-', '')
	if '-' in word and len(short_word) == 10 and short_word.isdigit:
		isbn_or_key = 'isbn'
	return isbn_or_key