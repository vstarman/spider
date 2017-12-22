#!usr/bin/env python
# -*- coding:utf-8 -*-
import pymongo
import json


class LaGouDB(object):
    def __init__(self, host, port):
        if not all([host, port]):
            host = '127.0.0.1'
            port = 27017
        self.host = host
        self.port = port

    def __open(self, file_name):
        self.json_file = open(file_name, 'r')

        # 创建MongoDB数据库连接,返回链接对象
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        # 指定数据库名称
        self.db = self.client['MongoDB_LaGou']
        # 指定集合名称
        self.collection = self.db['jobs']

    def __close(self):
        self.json_file.close()

    def run(self, file_name):
        try:
            # 1.创建文件操作对象,数据库操作对象
            self.__open(file_name)
            # 2.生成json对象
            json_obj = json.load(self.json_file)
            # 3.将数据写入数据库
            self.collection.insert(json_obj)
            # 4.关闭文件操作对象

            print '[叮咚]数据存储成功...'
        except Exception as e:
            print e
            print '[叮咚]数据存储失败...'

        self.__close()


if __name__ == '__main__':
    lago = LaGouDB('127.0.0.1', 27017)
    lago.run('北京_python_30_jobs.json')
