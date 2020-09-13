# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
from scrapy import signals
import time
import hashlib

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


# 生成随机 UA
class UserAgentMiddleware:
    '''
    自定义下载中间件
    随机的更换user-Agent
    '''

    def __init__(self):
        '''
        初始化
        '''
        self.ua = UserAgent()

    def process_request(self, request, spider):
        '''
        当请求对象传递给downloader之前，先要经过process_request方法预处理
        :param request:
        :param spider:
        :return:
        '''
        # print('=======UserAgentMiddleware process_request=======')
        # 随机获得一个ua值
        custom_ua = self.ua.random
        # print('custom_ua:', custom_ua)
        # 设置headers 的 ua
        request.headers.setdefault(b'User-Agent', custom_ua)


# 讯代理 IP
class ProxyIpMiddleware:
    '''
    随机的更换代理ip
    '''

    def __init__(self):
        '''
        初始化
        '''
        self.orderno = "ZF20209467227t2tXw"  # 订单号
        self.secret = "9129e49ebd314946b0078c39d6acf782"  # 秘钥

    def process_request(self, request, spider):
        print('===ProxyIpMiddleware process_request===')
        # 协议类型 B 站的为 HTTPS
        protocal = request.url.split(':')[0].strip()  # https
        timestamp = str(int(time.time()))  # 生成时间戳，单位是秒 1599183660

        # 用订单号，秘钥，时间戳拼接字符串
        string = "orderno=" + self.orderno + "," + "secret=" + self.secret + "," + "timestamp=" + timestamp
        string = string.encode()  # 字符串做编码
        # orderno=ZF201910273585ew6xSN,secret=1219111fc423464f9f1d3fde3ae6856a,timestamp=1597733722
        # b'orderno=ZF201910273585ew6xSN,secret=1219111fc423464f9f1d3fde3ae6856a,timestamp=1597733722'

        # 用md5生成摘要信息
        md5_string = hashlib.md5(string).hexdigest()  #
        sign = md5_string.upper()  # 4A2A285900B8EE014F6DFAF2DCC67923

        # 请求头认证信息
        auth = "sign=" + sign + "&" + "orderno=" + self.orderno + "&" + "timestamp=" + timestamp
        # sign=4A2A285900B8EE014F6DFAF2DCC67923&orderno=ZF201910273585ew6xSN&timestamp=1597733722
        request.headers['Proxy-Authorization'] = auth
        # request.headers['cookie'] = 'miid=1839296166129701888; cna=iWVdF+PvvQgCAXujeyj1sZ0u; t=831944179ae9dd36a06e2be50cf22ca9; lgc=aa1079146598; tracknick=aa1079146598; enc=GuY7NztxlkRbG%2Bf48q2eM9V%2Fhhmm601Uqy7HtcR8hxgDlO%2Ft9KDG31aijAMeBxsLK9o9mKYGJ6XxRCURIvWuag%3D%3D; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; xlly_s=1; _cc_=VT5L2FSpdA%3D%3D; mt=ci=103_1; _m_h5_tk=e51c2e269d29c42582bc6b896240a0dd_1599209142834; _m_h5_tk_enc=80a3ed1eb3bf842e2430e2e52e6fcbc2; _samesite_flag_=true; cookie2=1760a0300df997f2193126822aff0ffd; _tb_token_=3be1b8485beb3; sgcookie=EF8O1wpM7yLAo9Yy8i%2F2Z; unb=1972445289; uc1=cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie14=UoTV5Y5H3RHgng%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1; uc3=vt3=F8dCufXH%2BAMsh1wBUmQ%3D&id2=UojTVuIHb3zqpg%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&nk2=AnDVJEpmQvEXDU9j; csg=8142e389; cookie17=UojTVuIHb3zqpg%3D%3D; dnk=aa1079146598; skt=8b16c2bf5fd8c19c; existShop=MTU5OTIwMDg5Nw%3D%3D; uc4=id4=0%40UOBXV7AMoqMElHq0TcizrPqLpr%2Bf&nk4=0%40AJshffFDFK1Y4Y63k5hT%2BgmnQS0tlV0%3D; _l_g_=Ug%3D%3D; sg=89d; _nk_=aa1079146598; cookie1=VFIcudFooEItIV%2BdRtA%2BfyLVV2CjW2lQy7u0nwWdWks%3D; JSESSIONID=1CCAC7BA118AC320228BBC30DB27CBB4; tfstk=cRWVBIcPn-e2c09_9K9ZCVQ4JUOAaXscjY-Bi1YMRejLK4fw8sVtW32Hf3-6J8Ac.; l=eBQaK0q4Q8r0i-bCBO5Zourza77tFIRb4sPzaNbMiInca6sltFOIbNQ4hi7wSdtjgtC3TeKyOvlFRRLHR3cMVh9N33h2q_o-3xvO.; isg=BCYmjhlVReCfjBD9c9IxT5And5yoB2rBjJhzvxDPtckkk8ateZai0RSp648fO2LZ'
        ip = "forward.xdaili.cn"
        port = "80"
        ip_port = ip + ":" + port  # 代理ip转发地址
        proxy = {
            "http": "http://" + ip_port,
            "https": "https://" + ip_port
        }
        # 设置代理ip，
        request.meta['proxy'] = proxy[protocal]

# class Tieba1SpiderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Request or item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class Tieba1DownloaderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
