import pymysql.cursors
import hashlib, random , time

INSERTQUERY = 'INSERT INTO newsly (id, summary, title, brand, article_url, top_image, authors, publish_date, language, country, category, tags, trending) VALUES (\"%s\", \"\"\"%s\"\"\", \"\"\"%s\"\"\", \"%s\", \"%s\",\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")'


class SqlBuilder:
	@staticmethod
	def connect():
		connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='android',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
		return connection;

	@staticmethod
	def add(conn,summary, title, brand,article_url, top_image ,authors, publish_date, language, country, category, tags,is_trending ):
		cursor = conn.cursor()
		m = hashlib.md5()
		hashstring = title
		m.update(hashstring.encode('utf-8'))
		id = m.hexdigest()
		print(publish_date)

		sql = INSERTQUERY%(id,r''+summary.replace("'", "\\'").replace("\"","\\").replace("<p>", "").replace("</p>",""),
		                         r''+title.replace("'", "\\'").replace("\"","\\"),
		                         brand,
		                         article_url,
		                         top_image,
		                         authors,
		                         publish_date,
		                         
		                         language,
		                         country,
		                         category,
		                         tags,		                       
		                         str(is_trending)
		                         )

		try:
			cursor.execute(sql)
			conn.commit()
		except Exception as err:
			print("Mysql error :  %s"%err)
        	