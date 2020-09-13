import requests
from lxml import etree
import csv
import codecs
import time
import random
import pymysql
from fake_useragent import UserAgent

try:
    # 数据存储 mysql
    conn = pymysql.connect(host='localhost', port=3306, user="root", password="914673123", database="xiaoshuo")
    cur = conn.cursor()
    print("数据库 ok")
    start = int(input("请输入起始页："))
    end = int(input("请输入结束页："))
    tb_name = input("请输入贴吧名字：")
    # 贴吧后边是 f
    url = 'https://tieba.baidu.com/f'
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
    }
    for page in range(start, end + 1):
        print('page:', page)
        params = {
            'kw': tb_name,
            'ie': 'utf-8',
            'pn': (page - 1) * 50
        }
        response = requests.get(url, params=params, headers=headers)
        html = response.text

        # 二.数据提取
        html = etree.HTML(html)  # 二.内容解析 解析text
        ls = html.xpath('//li[@class=" j_thread_list clearfix"]')
        print(len(ls))
        for each in ls:
            # 标题
            title = each.xpath('.//a[@class ="j_th_tit "]/text()')[0]
            title = str(title)
            print("标题", title)
            print(type(title))

            # 回复数 .strip()移除首位空格
            answer_count = each.xpath('.//span[@class ="threadlist_rep_num center_text"]/text()')[0].strip()
            print("回复数", answer_count)

            # 作者
            author = each.xpath('.//span[@class ="frs-author-name-wrap"]/a/text()')[0].strip()
            print("作者", author)

            # 链接
            url_t = "https://tieba.baidu.com" + each.xpath('.//a[@class ="j_th_tit "]/@href')[0]
            print("链接", url_t)

            # # 数据存储.csv格式codecs.
            # # 第一步 打开
            # with codecs.open('./data/tieba_' + tb_name + '.csv', 'a', encoding='utf-8') as file:
            #     # 第二步 对csv操作，需要生成csv的writer对象
            #     wr = csv.writer(file)
            #     # 一般写法
            #     # wr.writerow([title, t3, t1, t2)
            #
            #     # 优化写法
            #     wr.writerow(f"标题：{title}")
            #     wr.writerow(f"链接：{answer_count}")
            #     wr.writerow(f"作者：{author}")
            #     wr.writerow(f"人数：{url_t}")
            #     wr.writerow("######################################")
            #     wr.writerow([title, answer_count, author, url_t])

            sql = "insert into tieba_one VALUE (0,%s,%s,%s,%s)"
            params = [title, answer_count, author, url_t]
            cur.execute(sql, params)
            conn.commit()
        time.sleep(random.random())
    time.sleep(random.random())


except Exception as e:
    print(e)
