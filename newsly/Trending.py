__author__ = "Vishal Jasrotia"
__copyright__ = ""
__credits__ = ["Vishal Jasrotia"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = "Testing"


import feedparser, time, newspaper
from fuzzywuzzy import fuzz
from newspaper.article import ArticleDownloadState


MATCH_RATIO = 55



_TRENIDNG_FEED = {
	# "us":"https://trends.google.com/trends/hottrends/atom/feed?pn=p1",
	# "uk":"https://trends.google.com/trends/hottrends/atom/feed?pn=p9",
	# "de":"https://trends.google.com/trends/hottrends/atom/feed?pn=p15",
	"us":"https://news.google.com/news/?gl=GB&ned=us&hl=en"
	#TODO add more
}


class Trending:
	"""
	"""
	@staticmethod
	def get_trends():
		"""
		"""
		_COUNTRY_VS_TREND = {}
		trending_title = []
		for _COUNTRY_CODE,  _TREND_FEED in _TRENIDNG_FEED.items(): 
			google = newspaper.build(_TREND_FEED)
			for article in google.articles:
				try:
					article.build()
					trending_title.append(article.title)
				except Exception:
					pass
			
		print(trending_title)
		time.sleep(20)
		return trending_title

	@staticmethod
	def is_trending(article, trending_title = [], last_trending =True):
		""" Article object from newspaper Article
		trends: result of get_trends()
		last_trending: True if no more new items required for current match
		"""
		if  article.download_state != ArticleDownloadState.SUCCESS  or not article.is_parsed:
			print("Err: Article is not downloaded or parsed.")
			return False
		for article_title in trending_title:

			if fuzz.ratio(article_title,article.title) >= MATCH_RATIO :
				
				print(article_title)
				#print(article.url)
				time.sleep(3)
				if last_trending:
					trending_title.remove(article_title)
				return True
		return False

		# for _COUNTRY_CODE, _TRENDING_LIST  in trends.items():
		# 	#if _COUNTRY_CODE == article.country #set attr in article for country
		# 	for _KEYWORD in _TRENDING_LIST:
		# 		if _KEYWORD.lower() in article.title.lower() or _KEYWORD in article.summary.lower():
		# 			if last_trending:
		# 				_COUNTRY_VS_TREND[_COUNTRY_CODE].remove(_KEYWORD) #ONE
		# 			return True
		# return False




		