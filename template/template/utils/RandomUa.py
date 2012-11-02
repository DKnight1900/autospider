#!/usr/bin/env python
#coding: utf-8

"""随机返回指定数据的 User-Agent.

以 json 格式返回，key 表示第几个 User-Agent，value 为具体的 User-Agent.

.. notes::

    * 隔一段时间得修改下 ua.txt 中的内容
"""

import sys
import json
from random import choice


class UserAgents(object):
    
    def __init__(self):
        print sys.path
        self.fn_ua = "defaulthome/utils/ua.txt"
        self.fp_ua = open(self.fn_ua, 'rb')
        
        self.ua_list = []
        for row in self.fp_ua:
            self.ua_list.append(row.strip())


    def __del__(self):
        self.fp_ua.close()

    
    def get_ua(self, num=1):
        """默认返回一个 User-Agent"""
        retvals = {}
        for i in xrange(num):
            retvals[i] = choice(self.ua_list)

        return json.dumps(retvals)


if __name__ == '__main__':
    """用于测试"""
    ua = UserAgents()
    print ua.get_ua(2)
    """
    返回的是类似于如下的数据，要注意 key 是个 str 而不是 num:

    {"0": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
     "1": "Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1"}
    """
