# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class Tieba1Pipeline:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='914673123', db='xiaoshuo')
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        strsql = 'insert into tieba_scr VALUES (0,%s,%s,%s,%s)'
        params = [item['title'], item['answer_count'], item['author'], item['url_t']]
        self.cur.execute(strsql, params)
        self.conn.commit()
        return item

    def close_spider(self, spdier):
        self.cur.close()
        self.conn.close()