#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re

import table
import tuple

class Translator(object):
	"""トランスレータ：総理大臣のCSVファイルをHTMLページへと変換するプログラム。"""

	def __init__(self, input_table):
		self.Table=input_table
		self.output_table = table.Table('output')

		"""トランスレータのコンストラクタ。"""
		return

	def compute_string_of_days(self, period):
		"""在位日数を計算して、それを文字列にして応答する。"""
		date = period.split("〜")
		if date[1] != '':
			d=datetime.datetime.strptime(date[1], '%Y年%m月%d日')
		else:
			d=datetime.datetime.today()
		d2=datetime.datetime.strptime(date[0], '%Y年%m月%d日')
		period=d-d2
		perioddate = period.days
		
		return str(perioddate)

	def compute_string_of_image(self, tuple):
		"""サムネイル画像から画像へ飛ぶためのHTML文字列を作成して、それを応答する。"""
		keys = self.Table.attributes().keys()
		No = str(tuple.dic['No'])
		Image = str(tuple.dic['Image'])
		Thumbnail = str(tuple.dic['Thumbnail'])
		print "aaaaa",tuple
		html = "<a name="+No+" href="+Image+"><img class=\"borderless\" src="+Thumbnail+" width=\"25\" height=\"32\" alt="+No+".jpg></a>"
		return html
	
	def table(self):
		"""総理大臣のCSVファイルを基にしたテーブルから、HTMLページを基にするテーブルに変換して、それを応答する。"""
		for n in self.Table.tuples():
			value=[]
			for i in self.output_table.attributes().keys():
				print 'table method', i, n.dic[i]
				if i !='Thumbnail':
					if i == 'Period':
						value.append(n.dic[i])
						days = self.compute_string_of_days(n.dic[i])
						n.dic['PeriodDays'] = days
					elif i == 'Image':
						value.append(self.compute_string_of_image(n))
					else:
						value.append(n.dic[i])
			a_tuple = tuple.Tuple(self.output_table.attributes(),value)
			self.output_table.add(a_tuple)
		return self.output_table
