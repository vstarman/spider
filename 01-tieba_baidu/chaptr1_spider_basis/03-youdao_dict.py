# -*- coding:utf-8 -*-
import urllib2
import urllib
import json
import random
import re
from tieba_floder.settings import MY_USER_AGENT

if __name__ == '__main__':
    while True:
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        headers = {"User-Agent": random.choice(MY_USER_AGENT)}
        words = raw_input('请输入要翻译的单词:')
        # 变动的是这两个参数，从start开始往后显示limit个
        # salt = "" + ((newDate).getTime() + parseInt(10 * Math.random(), 10))
        # sign = n.md5("fanyideskweb" + t + i + "aNPG!!u6sesA>hBAW1@(-");
        form_data = {
            'i': words,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '1513422483031',
            'sign': '8196a8760ea7656ec30548ddae197d77',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'true',
        }
        # 参数编码
        data = urllib.urlencode(form_data)

        request = urllib2.Request(url, data=data, headers=headers)
        response = urllib2.urlopen(request)

        resp_str = response.read()
        resp_dict = json.loads(resp_str)
        result = re.search(r'"tgt":"(.+)"', resp_str)
        print resp_str
        print result.group(1)
