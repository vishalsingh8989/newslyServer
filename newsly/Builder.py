__author__ = "Vishal Jasrotia"
__copyright__ = ""
__credits__ = ["Vishal Jasrotia"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = "Testing"


import newspaper
import time
import inputs.sources as news_sources
import logging

from newspaper.article import ArticleException
from newsly.Validater import Validate
from newsly.Trending import Trending


DEBUG = True

class NewsBuilder():
	"""
	"""
	def __init__(self, config):
		"""
		config : Configuration()
		"""
		self.news_source_url = news_sources.news_source_urls #newspaper.popular_urls()
		self.outfile = "C:\\workspace\\newslyServer\\outfile_"+str(int(time.time())) + ".txt"
		self.fd = open(self.outfile, 'w')
		self.source_vs_article_url = {}
		self.news_validater = Validate()
		self.trends = Trending.get_trends()
		self.config = config
		#print(self.trends)


	def build(self):
		""" Collect list of articles
		"""
		article_count = 0
		for url in self.news_source_url:

			#TODO META DATA SET IN RUNNER. create and pass Congif object from runner.py
			#config summary size.
			#self.config.get_language()
			paper = newspaper.build(url=url, dry=False, config=self.config)
			source_article_count = 0
			self.source_vs_article_url[url] = []
			for article in paper.articles:

				self.source_vs_article_url[url].append(article)

	def print_source_vs_article_url(self):
		"""
		"""
		if DEBUG:
			print("start print_source_vs_article_url ")
			
		for url, obj_article_list in self.source_vs_article_url.items():
			
			for obj_article in obj_article_list:
				#print(obj_article.url)
				try:
					obj_article.download()
					obj_article.parse()
					obj_article.nlp()
				except ArticleException as err:
					print("Err : %s"%err)
					continue
			#TODO 
			#find category
			#validate
			#calculate unique id using hashlib
			#run conitnuosly and learn category ML.
			#extract videos using video extarcter
				#print("Title :  %s\n"%obj_article.title.encode('utf-8'))
				if self.news_validater.validate_article(obj_article):
					try:# remove this after handling unicode string
						self.fd.write("*****************************\n")
						is_trending = Trending.is_trending(obj_article, self.trends, False)
						if is_trending :
							print(obj_article.title)
							print(obj_article.summary)
							print(obj_article.url)
							print("*************************")
							#time.sleep(1)
						self.fd.write("Trending : %s\n"%is_trending)
						self.fd.write("Title :  %s\n"%obj_article.title.encode('utf8'))
						self.fd.write("Summa :  %s\n"%obj_article.summary.encode('utf8'))
						self.fd.write(u"All Image : ")
						for img_path in obj_article.imgs:
							self.fd.write("%s\n"%img_path)
						self.fd.write("All movies : ")
						for mov_path  in obj_article.movies:
							self.fd.write("%s\n"%mov_path)
						self.fd.write(u"Keywords: %s\n"%obj_article.keywords)
						self.fd.write(u"Tags    : %s\n"%obj_article.tags)
						#self.fd.write("Metadata: %s"%obj_article.meta_data)
						self.fd.write("Top_image: %s\n"%obj_article.top_image.encode('utf8'))
						self.fd.write(u"Top_img  : %s\n"%obj_article.top_img)
						self.fd.write(u"Lang     : %s\n"%obj_article.meta_lang)
						self.fd.write(u"Author   : %s\n"%obj_article.authors)
						self.fd.write(u"Meta des : %s\n"%obj_article.meta_description.encode('utf8'))
					except UnicodeEncodeError as unicodeErr:
						self.fd.write(str(unicodeErr) + "\n")
					#time.sleep(5)
		
		self.fd.close()

	#def validate(self,article):







