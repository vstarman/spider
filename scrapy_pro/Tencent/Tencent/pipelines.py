# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime
from items import PositionItem, RequireItem


class TencentPipeline(object):
    """存储职位信息的管道"""
    def __init__(self):
        self.file_name = None

    def open_spider(self, *args):
        self.file_name = open('Tencent/data/tencent.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, PositionItem):
            item['source'] = spider.name
            item['crawl_time'] = str(datetime.utcnow())
            self.file_name.write(json.dumps(dict(item)) + ', \n')
        return item

    def close_spider(self, spider):
        self.file_name.close()


class RequirePipeline(object):
    """存储职位信息的管道"""
    def __init__(self):
        self.file_name = None

    def open_spider(self, *args):
        self.file_name = open('Tencent/data/tencent_require.json', 'w')
        self.file_name.write('[\n')

    def process_item(self, item, spider):
        if isinstance(item, RequireItem):
            item['source'] = spider.name
            item['crawl_time'] = str(datetime.utcnow())
            self.file_name.write(json.dumps(dict(item)) + ', \n')
        return item

    def close_spider(self, spider):
        self.file_name.write(']')
        self.file_name.close()
