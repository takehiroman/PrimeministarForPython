#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv

class IO(object):
	"""入出力：リーダ・ダウンローダ・ライタを抽象する。"""

	def read_csv(self, filename):
		reader=csv.reader(file(filename,'rU'))
		header = reader.next()
		list_reader=[]
		for n in reader:
			list_reader.append(n)
		"""指定されたファイルをCSVとして読み込む。"""
		return list_reader

	def write_csv(self, filename, rows):
		writer=csv.writer(file(filename,'rU'))
		for i in rows:
			writer.writerow(i)
		"""指定されたファイルにCSVとして行たち(rows)を書き出す。"""
		return
