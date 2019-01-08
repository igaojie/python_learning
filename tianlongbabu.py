# coding=utf-8
import jieba

with open('tianlongbabu_utf8.txt',errors='ignore',encoding='utf-8') as fp:
    lines = fp.readlines()

    for line in lines:
        seg_list = jieba.cut(line)
        with open('tianlongbabu_fenci.txt','a',encoding='utf-8') as ff:
            ff.write(' '.join(seg_list))