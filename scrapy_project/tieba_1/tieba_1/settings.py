# Scrapy settings for tieba_1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Scrapy项目的名字,这将用来构造默认 User-Agent
BOT_NAME = 'tieba_1'

SPIDER_MODULES = ['tieba_1.spiders']  # Scrapy搜索spider的模块列表 默认: [xxx.spiders]
NEWSPIDER_MODULE = 'tieba_1.spiders'  # 使用 genspider 命令创建新spider的模块。默认: 'xxx.spiders'

# 通过在用户代理上标识您自己（和您的网站）来负责地爬行
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

# Obey robots.txt rules (遵守robots.txt规则)
ROBOTSTXT_OBEY = False

# 配置Scrapy执行的最大并发请求（默认值：16）
# CONCURRENT_REQUESTS = 32

# 同一网站的请求配置延迟（默认值：0
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# 下载延迟
# DOWNLOAD_DELAY = 3

# 下载延迟设置将仅满足以下条件之一(二选一)
# CONCURRENT_REQUESTS_PER_DOMAIN = 16  # 每个域的并发请求的最大值
# CONCURRENT_REQUESTS_PER_IP = 16  # 对单个IP进行并发请求的最大值

# 禁用cookie（默认情况下启用）
# COOKIES_ENABLED = False

# 禁用telnet控制台（默认启用）
# TELNETCONSOLE_ENABLED = False

# 覆盖默认请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# 启用或禁用蜘蛛中间件
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tieba_1.middlewares.Tieba1SpiderMiddleware': 543,
# }

# 启用或禁用下载器中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'tieba_1.middlewares.Tieba1DownloaderMiddleware': 543,
# }

# 启用或禁用扩展
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 管道配置项目
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 启动管道
ITEM_PIPELINES = {
    'tieba_1.pipelines.Tieba1Pipeline': 300,
}

# 启用和配置AutoThrottle扩展（默认情况下禁用）
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True

# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies

# 在高延迟情况下设置的最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60

# Scrapy平均请求数应与每个远程服务器并行发送
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# 启用和配置HTTP缓存（默认情况下禁用）
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
