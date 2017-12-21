__author__ = "Vishal Jasrotia"
__copyright__ = ""
__credits__ = ["Vishal Jasrotia"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = "Testing"

import hashlib

from newspaper.article import ArticleDownloadState

DEBUG=True

class Validate():
	def __init__(self):
		#TODO save unique article id ids and check duplicate article
		# __hash__() in articles or maybe static list 
		self.article_id_list = []
		
	def validate_article(self, article):
		"""
		"""
		
		if not article.is_valid_body():
			return False
		if not article.is_valid_url():
			return False
		if not article.has_top_image():
			return False
		if len(article.authors) == 0 or len(article.authors) > 3: # usually not valid article bolgs etc.
			return False 
		if article.meta_lang == '' or article.meta_lang  is None:
			return False
		if article.download_state != ArticleDownloadState.SUCCESS:
			return False
		if article.top_image == '' or article.top_image is None:
			return False
		if article.publish_date is None or article.publish_date == '':
			return False
		if not article.is_parsed:
			return False
		return True

