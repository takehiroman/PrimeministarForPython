#! /usr/bin/env python
# -*- coding: utf-8 -*-

import attributes

class Table(object):
	"""表：総理大臣の情報テーブル。"""

	def __init__(self, kind_string):
		"""テーブルのコンストラクタ。"""
		self.attribute=attributes.Attributes(kind_string)
		self.tuple=[]
		"""入力用("input")または出力用("output")で属性リストを作成するコンストラクタ。"""
		
		return

	def __str__(self):
		s1='[\n'+self.attribute.__str__()+'\n,'
		s2=lambda x,y :x.__str__()+'\n,'+y.__str__()
		s3=reduce(s2,self.tuples())+'\n]'
		"""自分自身を文字列にして、それを応答する。"""
		return s1+s3

	def add(self, tuple):
		"""タプルを追加する。"""
		self.tuple.append(tuple)
		return

	def attributes(self):
		"""属性リストを応答する。"""
		return self.attribute

	def image_filenames(self):
		"""画像ファイル群をリストにして応答する。"""
		image_filenames=[]
		print self.attribute.keys()
		for n in self.tuples():
			image_filenames.append(n.dic['Image'])
#			dic=dict(zip(self.attribute.keys(), n))
#			image_filenames.append(dic["Image"])
		return image_filenames

	def thumbnail_filenames(self):
		"""縮小画像ファイル群をリストにして応答する。"""
		thumbnail_filenames=[]
		for n in self.tuples():
			thumbnail_filenames.append(n.dic['Thumbnail'])
#			dic=dict(zip(self.attribute.keys(),n))
#			thumbnail_filenames.append(dic["Thumbnail"])

		return thumbnail_filenames
	
	def tuples(self):
		"""タプル群を応答する。"""
		return self.tuple
