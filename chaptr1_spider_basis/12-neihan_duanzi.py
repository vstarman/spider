# -*- coding:utf-8 -*-
import re
import requests
import random
from my_user_poll import MY_USER_AGENT


class DuanziSpider(object):
    """内涵段子爬取"""

    def __init__(self):
        self.base_url = 'http://www.neihan8.com/article/list_5_%d.html'
        self.headers = {'User-Agent': MY_USER_AGENT[1]}
        self.page = 1
        # 匹配段子文本: re.S 开启DOTALL模式,匹配换行符
        self.pattern_page = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)
        self.pattern_jock = re.compile(r'<.*?>|&\w+?;|\s+|　+')

    def send_request(self, url):
        """
        :param url: 向url请求数据
        :return: 字节流
        """
        return requests.get(url, headers=self.headers).content

    def re_filter(self, html, file_obj):
        """
        :param html: 匹配html文件
        :param file_obj: 文件操作对象
        :return: 段子列表
                                    <p>
        老师:&ldquo;小明，你的梦想是什么？&rdquo;小明沉思片刻道:&ldquo;有房有铺，自己当老板，<br />
        妻子貌美如花，还有当官的兄弟&rdquo; 老师:北宋有个人和你一样，他姓武！</p>"""
        html = html.decode('gbk').encode('utf-8')
        # print type(html)
        jock_list = self.pattern_page.findall(html)
        for jock in jock_list:
            file_obj.write('"%s' % self.pattern_jock.sub('', jock) + '",\n')

    def star_work(self):
        """启动函数"""
        try:
            page = int(raw_input('内涵段子, 获取页数(每页10条):'))
            if not page:
                return '请输入页码'
            with open('12-jocks.py', 'a') as f:
                f.write('# -*- coding:utf-8 -*-\nMY_JOCKS = [\n')
                for i in range(1, page + 1):
                    url = self.base_url % self.page
                    html = self.send_request(url)
                    print '正在发送第%d页请求>>>>>' % i
                    self.re_filter(html, f)
                    self.page += 1
                f.write(']')

        except Exception as e:
            print e


if __name__ == '__main__':
    dz_spider = DuanziSpider()
    dz_spider.star_work()
