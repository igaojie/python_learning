# coding=utf-8
import requests
from bs4 import BeautifulSoup

# 抓取《大江大河》某一章节
def get_content(url):
    print(url)
    re_obj = requests.get(url)
    bs_obj = BeautifulSoup(re_obj.text.encode('utf8'), 'html.parser')

    content = bs_obj.find('div',{"id":"nr1"}).text
    return content


# 抓取《大江大河》入口
def get_all():
    re_obj = requests.get('http://www.luoxia.com/dajiangdahe/')
    bs_obj = BeautifulSoup(re_obj.text.encode('utf8'), 'html.parser')

    element = bs_obj.find('div', {"class": "book-list"}).find('ul').findAll('a')
    print(element)

    links = [a.attrs.get('href') for a in bs_obj.select('div.book-list ul a[href]')]

    for l in links:
        content = get_content(l)

        with open('dajiangdahe.txt', 'a', encoding='utf-8') as ff:
            ff.write(' ' + content)

# 对文本内容分词
def cut_content():
    import jieba

    jieba.load_userdict("dajiangdahe.dict.txt")
    with open('dajiangdahe.txt', errors='ignore', encoding='utf-8') as fp:
        lines = fp.readlines()

        for line in lines:
            seg_list = jieba.cut(line)
            with open('dajiangdahe_fenci.txt', 'a', encoding='utf-8') as ff:
                ff.write(' '.join(seg_list))


def create_model():
    from gensim.models import word2vec

    sentences = word2vec.Text8Corpus('dajiangdahe_fenci.txt')

    model = word2vec.Word2Vec(sentences)

    model.save('dajiangdahe.model')

def get_most():
    from gensim.models import word2vec

    model = word2vec.Word2Vec.load('dajiangdahe.model')
    for e in model.most_similar(positive=['雷东宝'],topn=30):
        print(e)


if __name__ == '__main__':
    # get_all()

    # cut_content()

    create_model()

    get_most()













