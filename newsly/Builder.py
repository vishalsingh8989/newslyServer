
import newspaper
import time


import logging

from newspaper.article import ArticleException

class NewsBuilder():
	def __init__(self):
		self.news_source_url = newspaper.popular_urls()
		self.outfile = "C:\\workspace\\outfile_"+str(time.time()) + ".txt"
		self.fd = open(self.outfile, 'w')
	def build(self):
		article_count = 0
		for url in self.news_source_url:
			config = newspaper.configuration.Configuration()
			config.memoize_articles = False
			paper = newspaper.build(url=url, dry=False, config=config)
			source_article_count = 0
			for article in paper.articles:
				try:
					article.download()
				except ArticleException:
					continue
				source_article_count+=1
				article_count+=1
				#article.download(input_html=None, title=None, recursion_counter=0)
			print("Url : %s ,  count %s"%(paper.brand, source_article_count))
		printf("Total : %s"%(article_count))







