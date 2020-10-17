# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#import sqlite3

import  mysql.connector



from itemadapter import ItemAdapter


class SpiderwhoPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        conn = mysql.connector.connect(
                    host='localhost',
                    user='admin',
                    password='openopen',
                    database='dbwho'
        )
        curs = conn.cursor()
        curs.execute("CREATE DATABASE my_db")
        print("------------------connect successful!!!------------------------------")

    def create_table(self):
        self.curs.execute("DROP TABLE IF EXISTS quotes_tb")

        self.sql=''' create table quotes_tb(
                         title text,
                         author text,
                         tag text) '''
        self.curs.execute(self.sql)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
          self.curs.execute(''' insert into quotes_tb values (%s, %s)''',(
              item['question'][0],
              item['response'][0]
          ))
          self.conn.commit()


