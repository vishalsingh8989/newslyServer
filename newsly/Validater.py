__author__ = "Vishal Jasrotia"
__copyright__ = ""
__credits__ = ["Vishal Jasrotia"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = "Testing"

import hashlib, calendar , datetime, time, random

from newspaper.article import ArticleDownloadState

DEBUG=True

INVALID_BODY = "Body of the article is Invalid!!"
INVALID_URL = "Invalid URL !!"
INVALID_TOP_IMAGE = "Invalid  top image!!"
INVALID_AUTHOR = "Invalid authors!!"
INVALID_META_LANG = "Invalid meta_lang !!"
INVALID_DOWNLOAD_STATE = "Err: Invalid download_state !!"
INVALID_PUB_DATE = "Err: Invalid publish date !!"
INVALID_PARSE = "Err :Article not parsed"
INVALID_TITLE = "Err: Invalid title"
INVALID_SUMMARY = "Err: Invalid summary"

NO_ERROR = "No_error"

MONTHS_NAME = ['Jan','January'  ,
'Feb','February',
'Mar','March'    ,
'Apr','April'    ,
'May'            ,
'Jun','June'     ,
'Jul','July'     ,
'Aug','August'   ,
'Sept','September',
'Oct','October'  ,
'Nov','November' ,
'Nov','December'] 


class Validate():
	def __init__(self):
		#TODO save unique article id ids and check duplicate article
		# __hash__() in articles or maybe static list 
		self.article_id_list = []
		
	def validate_article(self, article):
		"""
		"""
		ERROR = NO_ERROR
		if not article.is_valid_title():
			ERROR = INVALID_TITLE
		if not article.is_valid_summary():
			ERROR =INVALID_SUMMARY
		# if not article.is_valid_body(): dont use this. Test is not article.text not on article.summary
		# 	ERROR = INVALID_BODY	
		if not article.is_valid_url():
			ERROR  = INVALID_URL
		if not article.has_top_image():
			ERROR = INVALID_TOP_IMAGE
		if len(article.authors) == 0 or len(article.authors) > 2: # usually not valid article bolgs etc.and sometime month name are present in authors
			ERROR = INVALID_AUTHOR 
		if article.meta_lang == '' or article.meta_lang  is None:
			ERROR = INVALID_META_LANG
		if article.download_state != ArticleDownloadState.SUCCESS:
			ERROR = INVALID_DOWNLOAD_STATE
		if article.top_image == '' or article.top_image is None:
			ERROR = INVALID_TOP_IMAGE
		if article.publish_date is None or article.publish_date == '':
			#print("Invalid publish date: %s"%article.publish_date)
			ERROR = INVALID_PUB_DATE
			#article.publish_date = datetime.datetime.now() - datetime.timedelta(seconds= random.randint(3*3600 , 10*3600))
			#setattr(article, publish_date, datetime.datetime.now())
			#print("set : %s"%article.publish_date)
			#time.sleep(1)
		if not article.is_parsed:
			ERROR = INVALID_PARSE
		

		for m_name in MONTHS_NAME:
			for a_name in article.authors:
				 if m_name in a_name:
				 	ERROR = INVALID_AUTHOR 

		if ERROR != NO_ERROR:
			return False

		return True

