import matplotlib.pyplot as plt
from wordcloud import WordCloud
import stopwords

filename = 'data/steve.txt'
myfile = open(filename, 'rt', encoding='utf-8')

text = myfile.read()
print(type(text))

wc = WordCloud()
print(type(wc)) # <class 'wordcloud.wordcloud.WordCloud'>
wc = wc.generate(text) # return self
print(type(wc))
# print(wc)

# show
print(wc.words_)
print(type(wc.words_)) # return dict

bind = wc.words_
soredData = sorted(bind.items(),key=lambda x : x[1],reverse=True)
print(soredData)
print('-'*50)
chartData = soredData[0:10]
print(chartData)
# plt.bar(x=[x[0]for x in chartData],height=[x[1]for x in chartData])
# 도화지 사이즈 설정
plt.figure(figsize=(12,12))

plt.imshow(wc) # arg : WordCloud obj??
plt.savefig('concat_data/wordcl.png')
plt.show()
print('finished')

