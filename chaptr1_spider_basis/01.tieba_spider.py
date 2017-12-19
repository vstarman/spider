#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def send_request(url, file_name):
    """
    发送请求
    :param url:
    :param file_name:
    :return: html
    """
    print '正在下载' + file_name

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    request = urllib2.Request(url, headers=headers)
    # 发送一个url地址的请求,返回一个类文件的response对象
    response = urllib2.urlopen(request)
    # 编码为网站charset编码

    return response.read()


def save_file(html, file_name):
    """
    保存文件到本地
    :param html:
    :param file_name:
    :return:
    """
    print "正在存储" + file_name
    with open(file_name, 'w') as f:
        f.write(html)
    print "-" * 50


def spider_post_bar(key, begin_page, end_page):
    """爬取百度贴吧页面
    1.参数校验
    2.url合成
    3.发起请求
    4.保存静态资源
    :param key: 贴吧名称
    :param begin_page: 起始页
    :param end_page: 终止页
    :return:
    """
    # 1.参数校验
    assert all([key, begin_page, end_page]), Exception('请输入所需参数')
    assert (begin_page.isdigit() and end_page.isdigit()), Exception('起始与终止页必须为数字')

    # 2.url合成
    key = urllib.urlencode({'kw': key})
    b_page, e_page = int(begin_page), int(end_page)

    # 3.发起请求
    for page in range(b_page, e_page + 1):
        url = 'http://tieba.baidu.com/f?%s&ie=utf-8&pn=%d' % (key, (page - 1) * 50)
        file_name = '第' + str(page) + '页.html'
        # print file_name

        # 3.1 调用send_request,发起请求
        html = send_request(url, file_name)
        # 4.保存静态资源
        save_file(html, file_name)


if __name__ == '__main__':
    """获取参数"""
    keyword = raw_input('请输入要爬取的贴吧名: ')
    begin_page = raw_input('输入起始页: ')
    end_page = raw_input('输入终止页: ')
    # 抓取贴吧网页函数
    spider_post_bar(keyword, begin_page, end_page)
