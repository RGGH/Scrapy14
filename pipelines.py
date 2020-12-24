#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import sys
import mysql.connector
from mysql.connector import errorcode
from itemadapter import ItemAdapter
from datetime import datetime

# https://strftime.org/

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

class NewzzPipeline:

    def __init__(self):
        self.create_conn()
        self.create_table()
        
    def create_conn(self):
        # connect to Connect to DB
        try:
            self.conn = mysql.connector.connect(
                                    user = 'user1',
                                    password = 'password1',
                                    host = '192.168.1.9',
                                    port=3306,
                                    database = 'newz'
                                    )
        except mysql.error as e:
            print(f"Error connecting to DB platform : {e}")
            sys.exit(1)
            
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS tnewz""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS tnewz (
            id INT AUTO_INCREMENT PRIMARY_KEY,
            title VARCHAR(255),
            publication VARCHAR (30),
            author VARCHAR(50),
            story VARCHAR(255),
            url VARCHAR(100),
            posted TIMESTAMP
            )
            """)
                
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.store_db(item)
        
    def store_db(self,item):
        myquery = """INSERT into tnewz
        (
        title ,
        publication,
        author,
        story,
        url,
        posted
        )
        
        values (%s,%s,%s,%s,%s,%s)
        """
        val=(
        item.get('title'),
        item.get('publication'),
        item.get('author'),
        item.get('story'),
        item.get('url'),
        item.get('posted')
        
        )
        self.curr.execute(myquery,val)
        self.conn.commit()
        
    def close_spider(self, spider):
        self.conn.close()
