from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import jieba
import jieba.analyse
 
 
def jaccard_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))
    
    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    # 计算杰卡德系数
    return 1.0 * numerator / denominator
 
 
s1 = '你在干嘛呢'
s2 = '你在干什么呢'
print(jaccard_similarity(s1, s2))



strings = [
    '你在干什么',
    '你在干啥子',
    '你在做什么',
    '你好啊',
    '我喜欢吃香蕉'
]
 
target = '你在干啥'


print(list(filter(lambda x:jaccard_similarity(x,target) > 0,strings)))


for s in strings:
    print(jaccard_similarity(s,target))


content = '我的房子在方庄地铁附近的芳城园一区'

for i  in jieba.analyse.extract_tags(content, topK=20, withWeight=True):
    print(i)