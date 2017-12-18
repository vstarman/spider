# -*- coding:utf-8 -*-
import re
import requests
import random
from my_user_poll import MY_USER_AGENT


class DuanziSpider(object):
    """内涵段子爬取
    <div class="f18 mb20">
    <p>
    老师:&ldquo;小明，你的梦想是什么？&rdquo;小明沉思片刻道:&ldquo;有房有铺，自己当老板，<br />
    妻子貌美如花，还有当官的兄弟&rdquo; 老师:北宋有个人和你一样，他姓武！
    </p>
    </div>
    """
    def __init__(self):
        self.base_url = 'http://www.neihan8.com/article/list_5_%d.html'
        self.headers = {'User-Agent': random.choice(MY_USER_AGENT)}
        self.page = 1
        # re.S 开启DOTALL模式,匹配换行符
        self.pattern_content = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)

    def send_request(self):
        """发送请求"""
        url = self.base_url % self.page
        print url
        html = requests.get(url, headers=self.headers).content
        print html
        # txt = self.pattern_content.findall(html)
        # return txt

    def star_work(self):
        """启动函数"""
        while True:
            command = raw_input('按回车抓取段子(按Q退出):')
            if command == 'Q':
                break
            else:
                self.send_request()
            self.page += 1


if __name__ == '__main__':
    dz_spider = DuanziSpider()
    dz_spider.star_work()
