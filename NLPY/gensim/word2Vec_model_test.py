# 저장된 model 파일의 유사도를 이용한 시간화

import matplotlib.pyplot as plt
from gensim.models import word2vec
import numpy as np
plt.rc('font',family='Malgun Gothic')

def showGraph(bargraph):
    myticks = list(one[0] for one in bargraph)
    chartdata = list(one[1] for one in bargraph)
    mycolor = ['c', 'm', 'r', 'b', 'y','#56FFCC','#CCFF00','#CCDDEE','#FFCCDD','#123456']
    plt.barh(myticks,chartdata,color=mycolor,align='center')
    plt.show()
def makePie(piegraph):
    myticks = list(one[0] for one in piegraph)
    chartdata = list(one[1] for one in piegraph)
    mycolor = ['c','m','r','b','y']
    plt.pie(x=chartdata,labels=myticks,autopct='%1.2f%%',colors=mycolor)
    plt.show()
model_filename = 'data/word3vec.model'
model = word2vec.Word2Vec.load(model_filename)
print(type(model))
# 한국 + 중국 - 서울 = 북경
bargraph = model.most_similar(positive=['국민'], topn=10)
print(bargraph)

piegraph = model.most_similar(positive=['남북'], topn=5)
print(piegraph)

showGraph(bargraph)
makePie(piegraph)
# plt.show()