# coding=utf-8
from gensim.models import word2vec

#sentences = word2vec.Text8Corpus('tianlongbabu_fenci.txt')

#model = word2vec.Word2Vec(sentences)

#model.save('tianlongbabu.model')
model = word2vec.Word2Vec.load('tianlongbabu.model')
for e in model.most_similar(positive=['乔峰'],topn=10):
    print(e)


print(model.similarity('乔峰','慕容复'))

list1 = ['乔峰','慕容复']
list2 = ['萧远山','慕容博']
print(model.n_similarity(list1,list2))

list3 = ['乔峰', '段誉', '虚竹', '丁春秋']
print(model.doesnt_match(list3))

print(model['乔峰'])