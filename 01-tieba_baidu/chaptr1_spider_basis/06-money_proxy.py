# -*- coding:utf-8 -*-
import urllib2
import random
from tools.users import MY_USER_AGENT


def send_request():
    # 1.create free proxy
    # proxy = {}      # "origin": "211.103.136.242"
    # proxy = {'http': '120.27.218.32:16816'}    # 未认证
    # "origin": "120.27.218.32"
    proxy = {'http': 'mr_mao_hacker:sffqry9r@120.27.218.32:16816'}

    proxy_handler = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_handler)
    response = opener.open("http://www.httpbin.org/ip")

    # install_opener将指定的openre对象修改为全局opener
    urllib2.install_opener(opener)

    return response.read()


if __name__ == '__main__':
    print send_request()
