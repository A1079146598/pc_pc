from scrapy import cmdline
"""
用来启动 项目
"""
name = 'tieba_1_1'
cmd = f'scrapy crawl {name}'

cmdline.execute(cmd.split())
