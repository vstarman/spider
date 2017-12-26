# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # 爬取域名范围
    allowed_domains = ['baidu.com']
    # 第一批爬取的url
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print len(response.body)
        for xx in xxx:
            item = response.xpath('')
            yield item
        # pass
