"""
To test pyTagCloud
"""
def test1():
    from pytagcloud import create_tag_image, make_tags
    from pytagcloud.lang.counter import get_tag_counts

    YOUR_TEXT = "A tag cloud is a visual representation for text data, typically\
    used to depict keyword metadata on websites, or to visualize free form text."

    tags = make_tags(get_tag_counts(YOUR_TEXT), maxsize=80)

    create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')

    import webbrowser
    webbrowser.open('cloud_large.png')   # see results


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