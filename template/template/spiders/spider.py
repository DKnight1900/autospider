#!/usr/bin/env python
#coding: utf-8

"""
"""

import sys
import os
import time
import json
import re
from ConfigParser import ConfigParser

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.conf import settings
from scrapy.http import Request

from defaultcrawler.url.Urls import Urls
from defaultcrawler.db.MysqlHandler import MysqlHandler
from defaultcrawler.utils.RandomUa import UserAgents
from defaultcrawler.utils.tools import *

fn_config = 'config.ini'
config = ConfigParser()
config.read(fn_config)

reload(sys)
sys.setdefaultencoding('utf-8')

os.environ['TZ'] = config.get('TIME', 'timezone')
time.tzset()


class Crawler(BaseSpider):
    
    name = 'crawler'

    def __init__(self):
        global config

        self.confs_db = {
            'host': config.get('DB', 'host'),
            'user': config.get('DB', 'user'),
            'passwd': config.get('DB', 'passwd'),
            'db': config.get('DB', 'db'),
            }
        self.db = MysqlHandler(self.confs_db)

        self.urls = Urls()
        self.ua = UserAgents()
        self.httpheaders = {
            'Connection'     : 'keep-alive',
            'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Accept-Charset' : 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Cache-Control'  : 'max-age=0',
            'Referer'        : 'http://www.google.com',
            }

        settings.overrides['CONCURRENT_REQUESTS'] = config.get('SCRAPY', 'concurrent_requests')
        settings.overrides['CONCURRENT_REQUESTS_PER_DOMAIN'] = config.get('SCRAPY', 'concurrent_requests_per_domain')
        settings.overrides['DOWNLOAD_TIMEOUT'] = config.get('SCRAPY', 'download_timeout')

    def start_requests(self):
        headers = self.httpheaders
        for url in self.urls.get_urls():
            ua = json.loads(self.ua.get_ua())['0']
            headers['User-Agent'] = ua

            # 在这里可添加些要传给 callback 的参数,返入 meta 中, 如
            # meta = {'name': 'flyer', 'url_refer': url}
            meta = {}
            
            # 使用时修改下 callback 的函数名
            yield Request(url, headers=headers, meta=meta, callback=self.parse_origin)

    def parse_origin(self, response):
        """处理入口 url 返回的响应"""
        pass
