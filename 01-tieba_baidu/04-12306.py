# -*- coding:utf-8 -*-
import urllib2
import random
import ssl
from tieba_floder.settings import MY_USER_AGENT

if __name__ == '__main__':
    # 忽略ssl认证
    context = ssl._create_unverified_context()

    url = "https://www.12306.cn/mormhweb/"
    headers = {"User-Agent": random.choice(MY_USER_AGENT)}

    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, context=context)

    # ssl证书错误:urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] \
    # certificate verify failed (_ssl.c:590)>

    print response.read()
