# -*- coding: utf-8 -*-
import scrapy
import time
from Tencent.items import PositionItem, RequireItem
from scrapy.spiders import CrawlSpider, Rule


class Tx1Spider(scrapy.Spider):
    name = 'tx1'
    allowed_domains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/position.php?keywords=&lid=0&start='
    start_urls = [base_url + str(i) for i in range(0, 2681, 10)]

    # 1. 通过偏移量处理多个页面的规律情况
    # offset = 0
    # start_urls = [base_url + str(0)]

    def parse(self, response):
        """制作item传给pipelines做最后处理"""
        node_list = response.xpath("//tr[@class='odd'] | //tr[@class='even']")
        # print '-' * 100
        for node in node_list:
            item = PositionItem()
            item['position_link'] = 'http://hr.tencent.com/' + node.xpath('.//a/@href').extract_first()
            item['position_name'] = node.xpath('.//a/text()').extract_first()
            item['position_type'] = node.xpath('./td[2]/text()').extract_first()
            item['position_nums'] = node.xpath('./td[3]/text()').extract_first()
            item['work_location'] = node.xpath('./td[4]/text()').extract_first()
            item['publish_time'] = node.xpath('./td[5]/text()').extract_first()
            # time.sleep(0.1)
            print item['position_link']
            # meta 传递数据给callack函数
            yield scrapy.Request(url=item['position_link'], meta={'item': item}, callback=self.parse_page)
            yield item

    def parse_page(self, response):
        # item = response.meta['item']
        item = RequireItem()
        item['position_require'] = ''.join(response.xpath('//ul[@class="squareli"]')[0].xpath('./li/text()').extract())
        item['position_duty'] = ''.join(response.xpath('//ul[@class="squareli"]')[1].xpath('./li/text()').extract())
        print '-'*100
        yield item
