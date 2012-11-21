#!/usr/bin/env python
#coding:utf-8

import MySQLdb as mysqldb
import MySQLdb.cursors
from warnings import filterwarnings
filterwarnings('ignore', category=mysqldb.Warning)

class MysqlHandler(object):

    def __init__(self, conf, usedict=True):
        try:
            self.conf    = conf
            self.usedict = usedict

            if usedict:
                self.conn = mysqldb.connect(cursorclass=MySQLdb.cursors.DictCursor, **conf)
            else:
                self.conn = mysqldb.connect(**conf)

            self.conn.autocommit(True)
            self.cursor = self.conn.cursor()
        except Exception,e:
            print str(e)
            raise Exception('MysqlHandler init failed.')

        self.try_times = 0      # 纪录操作数据库出现异常时的次数


    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except:
            pass


    def exe(self, sql, params=()):
        try:
            self.cursor.execute(sql, params)
            if self.conn.affected_rows():
                self.try_times = 0
                return True
        except Exception,e:
            """尝试三次,若还有异常,则不再尝试"""
            self.try_times += 1
            if self.try_times > 3:
                print 'Error executing:\n  '+sql, '\n  params:', params, '\n  err info:', str(e)
                self.try_times = 0

                return False
            if str(e).lower().find('gone away')!=-1:
                self.__init__(self.conf)
                return self.exe(sql, params)
            print 'Error executing:\n  '+sql, '\n  params:', params, '\n  err info:', str(e)

        self.try_times = 0

        return False


    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    """用于测试"""
    confs = {
        'host': 'localhost',
        'user': 'user',
        'passwd': 'passwd',
        'db': 'db',
        }
    db = MysqlHandler(confs)

    sql = "SELECT id FROM sites WHERE name=%s"
    db.exe(sql, ('amazon', ))
    print db.cursor.fetchone()['id']
