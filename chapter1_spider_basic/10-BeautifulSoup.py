# -*- coding:utf-8 -*-
import requests
import chardet
from bs4 import BeautifulSoup, Tag
from my_user_poll import MY_USER_AGENT


def test():
    """Test model"""
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print soup.prettify()
    test_list = [
        'title--->', soup.title,
        'title.name--->', soup.title.name,
        'title.string--->', soup.title.string,
        'title.parent.name--->', soup.title.parent.name,
        'type(soup.p)--->', type(soup.p),
        'type(soup.p.decode())--->', type(soup.p.decode()),
        'soup.p["class"]--->', soup.p['class'],
        'type(soup.p["class"][0])--->', type(soup.p['class'][0]),
        'soup.a--->', {soup.a, type(soup.a)},
        'soup.find_all("a")--->', soup.find_all('a'),
        'soup.get_text()--->', soup.get_text(),
        'soup.p.attrs--->', soup.p.attrs,
        'soup.p.string--->', [soup.p.string, type(soup.p.string)],
        'soup.a.string--->', [soup.a.string, type(soup.a.string)],
        'soup.head.contents--->', [soup.head.contents[0], type(soup.head.contents)],
        'soup.head.children--->', [soup.head.children, type(soup.head.children)],
        'soup.descendants--->', [soup.descendants, type(soup.descendants)],
        'soup.find_all()--->', [i for i in soup.find_all()],
    ]
    # for i, show in enumerate(test_list):
    #     print show
    #     if i % 2 != 0:
    #         print '-' * 100
    print test_list.pop()
    print test_list.pop()
    # for child in soup.descendants:
    #     print child


class XpathTenCentJob(object):
    def __init__(self):
        from lxml import etree

    def run(self):
        pass


class Bs4TenCentJob(object):
    """爬取腾讯职位信息"""
    def __init__(self):
        self.base_url = 'http://hr.tencent.com/position.php?'
        self.headers = {'User-Agent': MY_USER_AGENT[1]}
        self.page = 0

    def run(self):
        for page in range(0, 2618, 10):
            full_url = self.base_url + str(page)
            html = self.send_request(full_url)

    def send_request(self, url):
        html = requests.get(url, self.headers)
        return html


if __name__ == '__main__':
    test()
