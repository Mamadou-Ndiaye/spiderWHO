# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#import sqlite3

import  mysql.connector



from itemadapter import ItemAdapter
import  pymongo

class SpiderwhoPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
                    'localhost',
                    27017
        )
        db = self.conn['dbwho']
        self.collection=db['who_tb']


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

