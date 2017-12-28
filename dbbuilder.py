import pymysql.cursors
import hashlib, random , time
import inputs.sources as news_sources
import newspaper
from newspaper.configuration import Configuration


INSERTQUERY = 'INSERT INTO brandinfo (code, name , meta_favicon, source_url) VALUES (\"%s\", \"%s\", \"\"\"%s\"\"\", \"\"\"%s\"\"\")'

news_source_url = news_sources.news_source_urls

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='android',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()


fd = open("query.txt", 'r')

for line in fd.readlines():
	print(line)
	cursor.execute(line)
# config = Configuration()
# config.memoize_articles = False # True in production
# for url in news_source_url:
# 	paper = newspaper.build(url=url, dry=False, config=config)
# 	for article in paper.articles:
# 		article.build()
# 		query = INSERTQUERY%(paper.brand, "Name" ,"Meta_favicon", paper.url)
# 		fd.write(query + "\n")
# 		break
connection.commit()
fd.close()




