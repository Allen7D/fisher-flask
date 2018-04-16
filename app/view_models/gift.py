# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/11.
"""
from app.view_models.book import BookViewModel

__author__ = 'Alimazing'

class MyGifts:
	def __init__(self, gifts_of_mine, wish_count_list):
		self.gifts = []

		self.__gifts_of_mine = gifts_of_mine
		self.__wish_count_list = wish_count_list

		self.gifts = self.__parse()
		pass

	def __parse(self):
		temp_gifts = []
		for gift in self.__gifts_of_mine:
			my_gift = self.__maching(gift)
			temp_gifts.append(my_gift)
		return temp_gifts

	def __maching(self, gift):
		count = 0
		for wish_count in self.__wish_count_list:
			if gift.isbn == wish_count['isbn']:
				count = wish_count['count']
		my_gift = {
			'book': BookViewModel(gift.book),
			'id': gift.id,
			'wishes_count': count
		}
		return my_gift