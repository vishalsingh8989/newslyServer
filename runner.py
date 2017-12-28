__author__ = "Vishal Jasrotia"
__copyright__ = ""
__credits__ = ["Vishal Jasrotia"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Vishal Jasrotia"
__email__ = "jasrotia.vishal@stonybrook.edu"
__status__ = "Testing"


from newsly.Builder import NewsBuilder
from newspaper.configuration import Configuration


if __name__ == "__main__":
	#pass config = Configuration()
	config = Configuration()
	config.memoize_articles = True # True in production
	config.MAX_AUTHORS = 2
	config.MIN_WORD_COUNT = 300
	#config.MAX_SUMMARY  = 900 on text .Not on summary . dont use it
	#TODO : Have a separate ArticleConfig and SourceConfig extend this!

	builder = NewsBuilder(config)
	builder.build()
	builder.print_source_vs_article_url()
