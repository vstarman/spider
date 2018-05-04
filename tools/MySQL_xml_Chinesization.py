# -*- coding:utf-8 -*-
import requests
import urllib
import json
import random
import re
from my_user_poll import MY_USER_AGENT


def translate_main(file_path, re_tag=None):
    """
    汉化文件
    :param file_path: 文件路径(格式为xml)
    :param re_tag: 正则(用来定位汉化单词)
    :return: 汉化后的文件
    """
    if not re_tag:
        re_tag = r'key="caption">(.*)</value>'
    try:
        re_group = re.match(r'(.*)(\..*)', file_path)
        new_path = re_group.group(1) + '-汉化版' + re_group.group(2)
        f_write = open(new_path, 'a+')
        with open(file_path, 'r') as f_read:
            for line_num, line in enumerate(f_read.readlines()):
                search_group = re.search(r'key="caption">(.*)</value>', line)
                # 定位需要汉化的单词,翻译
                if search_group:
                    old_word = search_group.group(1)
                    if '_' in old_word:
                        old_word = old_word.replace('_', '')
                    if '...' in old_word:
                        old_word = old_word.replace('...', '')
                    new_word = 'key="caption">' + word_translate(old_word) + '</value>'
                    line = re.sub(r'key="caption">(.*)</value>', new_word, line)

                f_write.write(line)
            print('---> 已写入第%d行 >>>' % line_num)
    except Exception as e:
        print(e)


# 单词翻译
def word_translate(words):
    """
    单词翻译
    :param words: 英文
    :return: 中文
    """
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    headers = {"User-Agent": random.choice(MY_USER_AGENT)}
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
    response = requests.post(url, data=form_data, headers=headers)

    resp_str = response.text
    resp_dict = json.loads(resp_str)
    chinese_word = resp_dict.get('translateResult')
    chinese_word = chinese_word[0][0].get('tgt')
    return chinese_word


if __name__ == '__main__':
    # word_translate('Report a Bug')
    translate_main('/home/python/Desktop/study/spider/static/main_menu.xml', 'a')
    pass
