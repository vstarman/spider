# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DyItem


class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ['http://capi.douyucdn.cn']
    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [url + str(offset)]

    def parse(self, response):
        # if response.body:
        data = json.loads(response.text)['data']
        if data:
            # print response.body
            item = DyItem()
            for i in data:
                item['name'] = i['nickname']
                item['image_url'] = i['room_src']

                yield item

            print '-' * 100
            print self.start_urls[0]
            # 每页100, 且自增
            self.offset += 100
            yield scrapy.Request(url=self.url + str(self.offset), callback=self.parse)
