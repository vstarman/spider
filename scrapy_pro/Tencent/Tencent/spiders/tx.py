# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import PositionItem, RequireItem


class TxSpider(scrapy.Spider):
    name = 'tx'
    allowed_domains = ['hr.tencent.com']
    start_url = ['http://http://hr.tencent.com/position.php?keywords=&lid=0&start=%d' % i for i in range(0, 2681, 10)]

    def parse(self, response):
        """制作item传给pipelines做最后处理"""
        node_list = response.xpath("//tr[@class='odd'] | //tr[@class='even']")
        for node in node_list:
            item = PositionItem()
            item['position_name'] = node.xpath('/td/a/@href').extract_first()
            item['position_link'] = node.xpath('/td/a/text()').extract_first()
            item['position_type'] = node.xpath('/td[2]/text()').extract_first()
            item['position_nums'] = node.xpath('/td[3]/text()').extract_first()
            item['work_location'] = node.xpath('/td[4]/text()').extract_first()
            item['publish_time'] = node.xpath('/td[5]/text()').extract_first()

            yield item
