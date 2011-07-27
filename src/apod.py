#!/usr/bin/env python
# encoding: utf-8
"""
apod.py

Created by Balfanz, Ryan on 2011-07-25.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

# import argparse
import unittest
import urllib2

from BeautifulSoup import BeautifulSoup


class PictureOfTheDay(object):
	"""docstring for PictureOfTheDay"""
	def __init__(self):
		super(PictureOfTheDay, self).__init__()
		
	def get_picture_of_the_day(self):
		"""docstring for get_picture_of_the_day"""
		raise NotImplementedError
		
		
class AstronomyPictureOfTheDay(PictureOfTheDay):
	"""docstring for AstronomyPictureOfTheDay"""
	def __init__(self):
		super(AstronomyPictureOfTheDay, self).__init__()
		self.url = "http://apod.nasa.gov/apod/astropix.html"
		self.html = None
		self.src = None
		self.img = None
		
	def get_apod(self):
		"""docstring for get_apod"""
		selector = "body.a.img"
		
		if not self.html:
			self.get_apod_html()
		else:
			pass
			
		assert self.html
			
		soup = BeautifulSoup(self.html)
		src = soup.findAll("img")[0]["src"]
		srcUrl = "/".join([self.url[:len(self.url)-self.url[::-1].index("/")], src])
		self.img = urllib2.urlopen(srcUrl).read()
		filename = "/tmp/" + src.split("/")[-1]
		with open(filename, "wb") as f:
			f.write(self.img)
		
		return filename
		
	def get_apod_url(self):
		"""docstring for get_picture_of_the_day"""
		return self.url
		
	def get_apod_html(self):
		"""docstring for get_apod_html"""
		self.html = urllib2.urlopen(self.url).read()
		return self.html
		
class PictureOfTheDayTests(unittest.TestCase):
	def setUp(self):
		self.flavors = {
			"vanilla": PictureOfTheDay(),
		}
		
	def test_base_class(self):
		"""docstring for fname"""
		vanillaInstance = self.flavors["vanilla"]
		self.assertRaises(NotImplementedError, vanillaInstance.get_picture_of_the_day)
		
if __name__ == '__main__':
	# unittest.main()
	
	# parser = argparse.ArgumentParser(description='Process some integers.')
	# parser.add_argument('integers', metavar='N', type=int, nargs='+',
	# 	help='an integer for the accumulator')
	# parser.add_argument('--sum', dest='accumulate', action='store_const',
	# 	const=sum, default=max,
	# 	help='sum the integers (default: find the max)')
	# 
	# args = parser.parse_args()
	# print args.accumulate(args.integers)
	
	apod = AstronomyPictureOfTheDay()
	# print apod.get_apod_url()
	# print apod.get_apod_html()
	print apod.get_apod()
	