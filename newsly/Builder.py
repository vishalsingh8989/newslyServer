
import newspaper
import time
import inputs.sources as news_sources

import logging

from newspaper.article import ArticleException

class NewsBuilder():
	def __init__(self):

		self.news_source_url = news_sources.news_source_urls #newspaper.popular_urls()
		#self.outfile = "C:\\workspace\\outfile_"+str(time.time()) + ".txt"
		#self.fd = open(self.outfile, 'w')
		self.source_vs_article_url = {}
	def build(self):
		article_count = 0
		
		for url in self.news_source_url:
			config = newspaper.configuration.Configuration()
			config.memoize_articles = False
			#TODO 
			#config summary size.
			#self.config.get_language()
			paper = newspaper.build(url=url, dry=False, config=config)
			source_article_count = 0
			self.source_vs_article_url[url] = []
			
			for article in paper.articles:
				self.source_vs_article_url[url].append(article)
				#print(), sep, end, file, flush)
				#print("********************************")
		# 		print(article.title)
		# 		print(article.config.get_language())
		# 		source_article_count+=1
		# 		article_count+=1
		# 		#article.download(input_html=None, title=None, recursion_counter=0)
		# 	print("Url : %s ,  count %s"%(paper.brand, source_article_count))
		# printf("Total : %s"%(article_count))
	def print_source_vs_article_url(self):
		for url, obj_article_list in self.source_vs_article_url.items():
			for obj_article in obj_article_list:
				try:
					obj_article.download()
					obj_article.parse()
					obj_article.nlp()
				except ArticleException as err:
					continue


				print("*****************************")
				print(dir(obj_article))
	#def validate(self,article):







