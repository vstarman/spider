# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import PositionItem
from scrapy.spiders import CrawlSpider, Rule


class TxSpider(scrapy.Spider):
    name = 'tx'
    allowed_domains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/position.php?keywords=&lid=0&start='
    start_urls = [base_url + str(i) for i in range(0, 2681, 10)]

    def parse(self, response):
        """制作item传给pipelines做最后处理"""
        node_list = response.xpath("//tr[@class='odd'] | //tr[@class='even']")
        print '-' * 100
        for node in node_list:
            item = PositionItem()
            item['position_link'] = node.xpath('./td/a/@href').extract_first()
            item['position_name'] = node.xpath('./td/a/text()').extract_first()
            item['position_type'] = node.xpath('./td[2]/text()').extract_first()
            item['position_nums'] = node.xpath('./td[3]/text()').extract_first()
            item['work_location'] = node.xpath('./td[4]/text()').extract_first()
            item['publish_time'] = node.xpath('./td[5]/text()').extract_first()
            print '-' * 100
            print item
            yield item
