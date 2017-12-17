# -*- coding:utf-8 -*-

import urllib2

# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
# http-->https才能打印
http_proxy_handler = urllib2.ProxyHandler({"https": "124.88.67.81:80"})
null_proxy_handler = urllib2.ProxyHandler({})


# 定义一个代理开关
proxy_switch = True

# 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
if proxy_switch:
    opener = urllib2.build_opener(http_proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

request = urllib2.Request('http://www.baidu.com')

# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
# response = opener.open(request)

# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
urllib2.install_opener(opener)
response = urllib2.urlopen(request)

print response.read()

