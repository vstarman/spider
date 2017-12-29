# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DyItem


class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ['douyucdn.cn']
    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [url + str(offset)]

    def parse(self, response):
        # if response.body:
        data = json.loads(response.text)['data']
        if data:
            for i in data:
                item = DyItem()
                item['name'] = i['nickname']
                item['image_url'] = i['room_src']

                yield item

            # 每页100, 且自增
            self.offset += 20
            print '-' * 100
            print self.url + str(self.offset)
            yield scrapy.Request(url=self.url + str(self.offset), callback=self.parse)


class DyPipeline(object):
    def __init__(self):
        # 获取setting主机名、端口号和数据库名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        # pymongo.MongoClient(host, port) 创建MongoDB链接
        client = pymongo.MongoClient(host=host,port=port)

        # 指向指定的数据库
        mdb = client[dbname]
        # 获取数据库里存放数据的表名
        self.post = mdb[settings['MONGODB_DOCNAME']]