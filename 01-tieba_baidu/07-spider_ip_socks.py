#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 爬取免费代理ip,
import urllib2
import urllib
import sys
import random
from tieba_floder.settings import MY_USER_AGENT
reload(sys)
sys.setdefaultencoding('utf-8')


# 定义一个代理开关
proxy_switch = True


def proxy_handler():
    """
    构建代理
    :return:
    """
    # 构建了两个代理Handler，一个有代理IP，一个没有代理IP
    # http-->https才能打印
    http_proxy_handler = urllib2.ProxyHandler({"https": "124.88.67.81:80"})
    null_proxy_handler = urllib2.ProxyHandler({})

    # 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
    # 根据代理开关是否打开，使用不同的代理模式
    if proxy_switch:
        opener = urllib2.build_opener(http_proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    return opener


def send_request(url, file_name, headers):
    """
    发送请求
    :param url:
    :param file_name:
    :return: html
    """
    print '--------->正在下载: ' + file_name

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
    print "--------->正在存储: " + file_name
    with open(file_name, 'w+') as f:
        f.write(html)
    print "-" * 50


def spider_post_bar():
    """爬取百度贴吧页面
    3.发起请求
    4.保存静态资源
    :return:
    """
    file_name = '快代理1-50.txt'
    # html = ''
    for i in range(1, 51):
        # 3.1 调用send_request,发起请求
        headers = {"User-Agent": random.choice(MY_USER_AGENT)}
        url = 'http://www.kuaidaili.com/free/intr/%d' % i
        html = send_request(url, file_name, headers)
        # 4.保存静态资源TODO??????
        save_file(html, file_name)


if __name__ == '__main__':
    """获取参数"""
    # 抓取贴吧网页函数
    # spider_post_bar()

    file_name = '快代理1-50.txt'
    headers = {
        "Cookie": "yd_cookie=88ac7258-89f8-423bed8e6244513c143676d2aaeb658894a0; \
                _ydclearance=6d7ceb652373adc945d9c533-4963-4914-8bf6-3ece60067acc-1513510636; \
                _ga=GA1.2.1128972144.1513503518; _gid=GA1.2.1937102265.1513503518; \
                Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1513503518; \
                Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1513503518",
        "Host": "www.kuaidaili.com",
        "User-Agent": random.choice(MY_USER_AGENT)
    }

    # print random.choice(MY_USER_AGENT)
    url = 'http://www.kuaidaili.com/free/inha/'

    request = urllib2.Request(url, headers=headers)
    # 发送一个url地址的请求,返回一个类文件的response对象

    response = urllib2.urlopen(request)

    print response.read()
    # with open(file_name, 'w') as f:
    #     f.write(response)
    # print "-" * 50


