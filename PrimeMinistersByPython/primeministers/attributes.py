#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Attributes(object):
	"""属性リスト：総理大臣の情報テーブルを入出力する際の属性情報を記憶。"""

	def __init__(self, kind_string):
		if(kind_string=='input'):
			self.list_keys=['No','Order','Name','Kana','Period','School','Party','Place','Image','Thumbnail']
		else:
			self.list_keys=['No','Order','Name','Kana','Period','PeriodDays','School','Party','Place','Image']
		"""入力用("input")または出力用("output")で属性リストを作成するコンストラクタ。"""
		self.Name=[]
		return

	def __str__(self):
		s='[' + ','.join(self.list_keys)+']'
		"""自分自身を文字列にして、それを応答する。"""
		return s

	def keys(self):
		"""キー群を応答する。"""
		return self.list_keys

	def names(self):
		"""名前群を応答する。"""
		return self.Name

	def set_names(self, names):
		"""名前群を設定する。"""
		self.Name=names
		return


