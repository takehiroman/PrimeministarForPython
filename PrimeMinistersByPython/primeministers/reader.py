#! /usr/bin/env python
# -*- coding: utf-8 -*-

import io
import table
import tuple

class Reader(io.IO):
	"""リーダ：総理大臣の情報を記したCSVファイルを読み込んでテーブルに仕立て上げる。"""

	def __init__(self, csv_filename):
		"""リーダのコンストラクタ。"""
		self.csv_filename=csv_filename
		return

	def table(self):
		"""ダウンロードしたCSVファイルを読み込んでテーブルを応答する。"""
		list_reader=io.IO().read_csv(self.csv_filename)
		input_table = table.Table('input')
		for n in list_reader:
			a_tuple = tuple.Tuple(input_table.attributes(), n)
			input_table.add(a_tuple)
		return input_table
