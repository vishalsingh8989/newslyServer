__author__ = "Vishal Jasrotia"
__copyright__ = ""
__credits__ = ["Vishal Jasrotia"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = "Testing"


import feedparser
from newspaper.article import ArticleDownloadState



_TRENIDNG_FEED = {
	"us":"https://trends.google.com/trends/hottrends/atom/feed?pn=p1",
	"uk":"https://trends.google.com/trends/hottrends/atom/feed?pn=p9",
	"de":"https://trends.google.com/trends/hottrends/atom/feed?pn=p15"

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
		for _COUNTRY_CODE,  _TREND_FEED in _TRENIDNG_FEED.items(): 
			try:
				listing = feedparser.parse(_TREND_FEED)['entries']
				trends = [item['title'] for item in listing]
				_COUNTRY_VS_TREND[_COUNTRY_CODE] = trends
				print(trends)
			except Exception as e:
				print('ERR Trending terms failed!', str(e))
				pass
		return _COUNTRY_VS_TREND

	@staticmethod
	def is_trending(article, trends = {}, last_trending =True):
		""" Article object from newspaper Article
		trends: result of get_trends()
		last_trending: True if no more new items required for current match
		"""
		if  article.download_state != ArticleDownloadState.SUCCESS  or not article.is_parsed:
			print("Err: Article is not downloaded or parsed.")
			return False
		for _COUNTRY_CODE, _TRENDING_LIST  in trends.items():
			#if _COUNTRY_CODE == article.country #set attr in article for country
			for _KEYWORD in _TRENDING_LIST:
				if _KEYWORD.lower() in article.title.lower() or _KEYWORD in article.summary.lower():
					if last_trending:
						_COUNTRY_VS_TREND[_COUNTRY_CODE].remove(_KEYWORD) #ONE
					return True
		return False




		