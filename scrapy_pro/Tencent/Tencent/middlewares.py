# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from settings import USER_AGENT_LIST


# 处理user-agent
class UserAgentMiddleware(object):
    """设置用户user-agent的类"""
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent


# 处理proxy代理
class ProxyMiddleware(object):
    """设置用户user-agent的类"""
    def process_request(self, request, spider):
        proxy = "http://mr_mao_hacker:sffqry9r@120.27.218.32:16816"
        request.meta["proxy"] = proxy
