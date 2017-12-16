# -*- coding:utf-8 -*-
import urllib2
import random
import ssl
from tieba_floder.settings import MY_USER_AGENT

if __name__ == '__main__':
    while True:
        url = "https://www.12306.cn/mormhweb/"
        headers = {"User-Agent": random.choice(MY_USER_AGENT)}

        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)

        # ssl证书错误:urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] \
        # certificate verify failed (_ssl.c:590)>

        print request.read()
