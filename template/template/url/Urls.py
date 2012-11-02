#!/usr/bin/env python
#coding: utf-8

"""提供入口页 url

目前提供三种接口,即 `get_urls()` `get_urls_db()` `get_urls_file()`,分别表示从
类的某个 list 类型中读取初始 urls, 从数据库中读取初始 urls, 从文件中读取 urls.使用
是需要改写这三个方法
"""

class Urls(object):
    
    def __init__(self):
        self.url_entry = [
            # 图书
            'http://www.360buy.com/book/booksort.aspx',
            # 音乐
            'http://mvd.360buy.com/mvdsort/4051.html',
            # 影视
            'http://mvd.360buy.com/mvdsort/4052.html',
            ]

    def get_urls(self):
        """读取 `__init__()` 方法设定好的 urls"""
        for url in self.url_entry:
            yield url

    def get_urls_db(self):
        """从数据库中读取 urls, 通过 `yield` 方式返回每条数据"""
        pass

    def get_urls_file(self):
        """从文件中读取 urls, 通过 `yield` 方式返回每条数据"""
        pass


if  __name__ == '__main__':
    """仅为了测试"""
    urls = Urls()
    for url in urls.get_urls():
        print url
