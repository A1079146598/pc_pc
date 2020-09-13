import scrapy


class Tieba11Spider(scrapy.Spider):
    name = 'tieba_1_1'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/']

    def parse(self, response):
        print("666666666666666")
