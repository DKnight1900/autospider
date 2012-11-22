#!/usr/bin/env python
#coding: utf-8

"""提供常用的函数
"""

import time
import os
from ConfigParser import ConfigParser

fn_config = 'config.ini'
config = ConfigParser()
config.read(fn_config)
timezone = config.get('TIME', 'timezone')

os.environ['TZ'] = timezone
time.tzset()

def sqltime(formate):
    """
    :param str formate: 可取 `date` `datetime`
    :return: str 类型的时间
    """
    if formate == 'datetime':
        rettime = time.strftime('%Y-%m-%d %X')
    elif formate == 'date':
        rettime = time.strftime('%Y-%m-%d')
        
    return rettime    

def trimwords(word):
    wleft = ''
    word = word.strip()
    while word:
        word_list = word.partition(' ')
        wleft = '%s%s' % (wleft, word_list[0])
        word = word_list[2].strip()

    return wleft

def handle_url(url, base_url):
    """把 `base_url` 的格式统一为 `http://www.dangdang.com` 形式"""
    if base_url.endswith('/'):
        base_url = base_url[:-1]

    if url.startswith('http'):
        return url
    elif url.startswith('/'):
        return '%s%s' % (base_url, url)
    else:
        return '%s/%s' % (base_url, url)


if __name__ == '__main__':
    """用于测试"""
    print sqltime('datetime')
    print sqltime('date')

    print trimwords('   gsdf  gfds   ')
    print handle_url('/test.html', 'http://www.amazon.cn')
    print handle_url('test.html', 'http://www.amazon.cn/')
    print handle_url('http://www.amazon.cn', 'http://www.amazon.cn')
