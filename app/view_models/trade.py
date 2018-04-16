# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/13.
"""
from app.view_models.book import BookViewModel

__author__ = 'Alimazing'

class TradeInfo:
	def __init__(self, goods):
		self.total = 0
		self.trades = []
		self.__parse(goods)

	def __parse(self, goods):
		self.total = len(goods)
		self.trades = [self.__map_to_trade(single) for single in goods]

	def __map_to_trade(self, single):
		if single.create_datetime:
			time = single.create_datetime.strftime('%Y-%m-%d')
		else:
			time = '未知'
		return dict(
			user_name = single.user.nickname,
			time = time,
			id = single.id
		)

class MyTrades:
	def __init__(self, trades_of_mine, trade_count_list):
		self.trades = []

		self.__trades_of_mine = trades_of_mine
		self.__trade_count_list = trade_count_list

		self.trades = self.__parse()
		pass

	def __parse(self):
		temp_trades = []
		for trade in self.__trades_of_mine:
			my_trade = self.__maching(trade)
			temp_trades.append(my_trade)
		return temp_trades

	def __maching(self, trade):
		count = 0
		for trade_count in self.__trade_count_list:
			if trade.isbn == trade_count['isbn']:
				count = trade_count['count']
		my_trade = {
			'book': BookViewModel(trade.book),
			'id': trade.id,
			'trades_count': count
		}
		return my_trade