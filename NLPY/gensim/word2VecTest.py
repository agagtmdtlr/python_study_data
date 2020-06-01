from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec
# import smart_open.gcs

file = open('data/문재인대통령신년사.txt','rt',encoding='utf-8')
soup = BeautifulSoup(file,'html.parser')
mydata = soup.text
# print(mydata)


okt = Okt()
result = [] # 결과를 저장할 리스트
datalines = mydata.split('\n')
for oneline in datalines:
    mypos = okt.pos(oneline,norm=True,stem=True)
    imsi = []

    for word in mypos :
        # ( 단어 , 품사 )
        if not word[1] in ['Josa','Eomi','Punctuation','Verb']:
            if len(word[0]) >= 2 :
                imsi.append(word[0])

    temp = (' '.join(imsi)).strip()
    result.append(temp)

print(len(result))

result_file = 'data/word2vec.prepro'

with open(result_file,'wt',encoding='utf-8') as myfile:
    myfile.write('\n'.join(result))

print(result_file + '파일 저장됨')

# 모델 만들기
sentence = word2vec.LineSentence(source=result_file)
print(type(sentence))

model = word2vec.Word2Vec(sentence, size=200,window=10, hs=1, min_count=2, sg=1)
print(type(model))

model_filename = 'data/word3vec.model'
model.save(model_filename)
print(model_filename + ' 파일 저장됨')
print('finished')