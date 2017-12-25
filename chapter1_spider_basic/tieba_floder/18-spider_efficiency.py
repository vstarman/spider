#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
用来测试python提升爬虫并发量各种方法的优缺点
"""
import thread
import requests
import time
from lxml import etree


class SpiderDB250(object):
    """爬取豆瓣电影250"""
    def __init__(self):
        self.start_url = ['https://movie.douban.com/top250?start=%d' % i for i in range(0, 226, 25)]
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/63.0.3239.84 Safari/537.36'}
        # self.prox =

    def send_request(self, url):
        """发送请求,且将响应对象传parse_page解析"""
        response = requests.get(url, headers=self.headers)
        self.parse_page(response)

    def parse_page(self, response):
        """解析页面返回列表"""
        html_obj = etree.HTML(response.content)
        note_list = html_obj.xpath("//div[@class='info']")
        for note in note_list:
            item = dict()
            item['name'] = note.xpath("./div[@class='hd']/a/span[1]/text()")[0]
            item['score'] = note.xpath("./div[@class='bd']/div[@class='star']/span[2]/text()")[0]
            item['detail'] = note.xpath("./div[@class='bd']/p[1]/text()")[0]
            print '%s \t %s' % (item['score'], item['name'])
            time.sleep(1)

    def run(self):
        start_time = time.time()
        for url in self.start_url:
            self.send_request(url)
        print '[info]共用时: %ds ' % (time.time() - start_time)
# 总结点
# //div[@class='info']
# 电影名
# ./div[@class='hd']/a/span[1]/text()
# 电影评分
#
# 导演
# ./div[@class='bd']/p[1]/text()


if __name__ == '__main__':
    dou_ban = SpiderDB250()
    dou_ban.run()
