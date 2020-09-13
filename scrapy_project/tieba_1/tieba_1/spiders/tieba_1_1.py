import scrapy
from urllib import parse
from scrapy_project.tieba_1.tieba_1.items import Tieba1Item
from lxml import etree


class Tieba11Spider(scrapy.Spider):
    name = 'tieba_1_1'
    what = "杭州"
    what = parse.quote(what)
    allowed_domains = ['tieba.baidu.com']
    start_urls = [f'http://tieba.baidu.com/f?kw={what}&ie=utf-8&pn=0']
    page = 0
    # 爬的页数
    page_nums = 5

    def parse(self, response):
        self.page += 1
        print(f"第{self.page}页")
        # print(response.text).

        ls = response.xpath('//ul[@id="thread_list"]/li[@class=" j_thread_list clearfix"]')
        print(len(ls))

        for each in ls:
            item = Tieba1Item()
            item['title'] = each.xpath('.//a[@class ="j_th_tit "]/text()').extract()[0]
            item['answer_count'] = each.xpath('.//span[@class ="threadlist_rep_num center_text"]/text()').extract()[0]
            item['author'] = each.xpath('.//span[@class ="frs-author-name-wrap"]/a/text()').extract()[0].strip()
            item['url_t'] = response.url
            yield item

        if self.page <= self.page_nums-1:
            url = f'http://tieba.baidu.com/f?kw={self.what}&ie=utf-8&pn={(self.page) * 50}'
            print('next_page_url:', url)
            yield scrapy.Request(url, callback=self.parse)

