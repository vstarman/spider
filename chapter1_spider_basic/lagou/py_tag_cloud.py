# -*- coding:utf-8 -*-
"""
To test pyTagCloud
"""
import sys
sys.path.append('../')
import jieba
import jieba.analyse
from optparse import OptionParser


def test1():
    from pytagcloud import create_tag_image, make_tags
    from pytagcloud.lang.counter import get_tag_counts

    f = file('./北京_python_30_jobs.json', 'r')
    YOUR_TEXT = f.read()

    tags = make_tags(get_tag_counts(YOUR_TEXT), maxsize=80)

    create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')

    import webbrowser
    webbrowser.open('cloud_large.png')   # see results

    f.close()


def test2():
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    import jieba

    text_from_file_with_apath = open('/Users/hecom/23tips.txt').read()

    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)

    my_wordcloud = WordCloud().generate(wl_space_split)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()


def jie_ba():
    USAGE = "usage:    python extract_tags_with_weight.py [file name] -k [top k] -w [with weight=1 or 0]"

    parser = OptionParser(USAGE)
    parser.add_option("-k", dest="topK")
    parser.add_option("-w", dest="withWeight")
    opt, args = parser.parse_args()

    if len(args) < 1:
        print(USAGE)
        sys.exit(1)

    file_name = args[0]

    if opt.topK is None:
        topK = 10
    else:
        topK = int(opt.topK)

    if opt.withWeight is None:
        withWeight = False
    else:
        if int(opt.withWeight) is 1:
            withWeight = True
        else:
            withWeight = False

    content = open(file_name, 'rb').read()

    tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)

    if withWeight is True:
        for tag in tags:
            print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
    else:
        print(",".join(tags))


if __name__ == '__main__':
    jie_ba()
