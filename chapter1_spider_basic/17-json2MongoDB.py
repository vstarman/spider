#!usr/bin/env python
# -*- coding:utf-8 -*-
import pymongo


class LaGouDB(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __open(self):
        self.json_file = open('', 'r')

        # 创建MongoDB数据库连接,返回链接对象
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        # 指定数据库名称
        self.db = self.client['MongoDB_LaGou']
        # 指定集合名称
        self.collection = self.db['jobs']

    def __close(self):
        self.json_file.close()



if __name__ == '__main__':
    lago = LaGouDB('127.0.0.1', 27017)

