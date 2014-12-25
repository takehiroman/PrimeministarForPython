#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import urllib

import io
import reader

class Downloader(io.IO):
	"""ダウンローダ：総理大臣のCSVファイル・画像ファイル・サムネイル画像ファイルをダウンロードする。"""

	def __init__(self, base_directory):
		"""ダウンローダのコンストラクタ。"""
		self.base_directory=base_directory
		self.url ='http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/CSV2HTML/PrimeMinisters/'
		self.image_directory=os.path.join(self.base_directory,'images')
		os.makedirs(self.image_directory)
		self.thumbnails_directory=os.path.join(self.base_directory,'thumbnails')
		os.makedirs(self.thumbnails_directory)
		return

	def download_all(self):
		self.download_csv()
		read=reader.Reader(os.path.join(self.base_directory, 'PrimeMinisters.csv'))
		table=read.table()
		list_image=table.image_filenames()
		list_thumbnail=table.thumbnail_filenames()
		self.download_images(list_image)
		self.download_images(list_thumbnail)
		
		"""すべて（総理大臣の情報を記したCSVファイル・画像ファイル群・縮小画像ファイル群）をダウンロードし、テーブルを応答する。"""
		return table

	def download_csv(self):
		"""総理大臣の情報を記したCSVファイルをダウンロードする。"""
		try:
			urllib.urlretrieve('http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/CSV2HTML/PrimeMinisters/PrimeMinisters.csv',os.path.join(self.base_directory, 'PrimeMinisters.csv'))
		except IOError:
			print "IOError"
		return 

	def download_images(self,image_filenames):
		try:
			for n in image_filenames:
				urllib.urlretrieve('http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/CSV2HTML/PrimeMinisters/'+n,os.path.join(self.base_directory, n))
		except IOError:
			print "IOError"
		"""画像ファイル群または縮小画像ファイル群をダウンロードする。"""
		return
