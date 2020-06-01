import nltk # national language tool-kit
import numpy as np
import matplotlib.pyplot as plt

from pandas import DataFrame
from konlpy.tag import Okt
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from PIL import Image

plt.rc('font',family='Malgun Gothic')

class Visualization:
    def __init__(self,wordList):
        self.wordList = wordlist
        self.wordDict = dict(wordlist)

    def makeWordCloud(self):
        plt.figure(figsize=(8,8))
        alice_file = 'data/alice_color.png'
        # 이미지 파일을 가져오는 방법 PIL.Image.open(file) :pilimageObj
        # np.array(pilimageObj)
        pilImage = Image.open(alice_file)
        print(type(pilImage))
        print(pilImage.getdata())
        alice_mask = np.array(pilImage)

        alice_color = ImageColorGenerator(alice_mask)
        wc = WordCloud(font_path='malgun.ttf', mask=alice_mask,
                       background_color='white', random_state=43)
        wc = wc.generate_from_frequencies(self.wordDict)
        wc = wc.recolor(color_func=alice_color,random_state=43)

        plt.imshow(wc)

        filename = 'data/tojiText_wc.png'
        plt.savefig(filename)
    

    # end class makeWordCloud
    def makeBarChart(self):
        plt.figure(figsize=(8,8))
        word_top = sorted(self.wordDict.items(), key=lambda x : x[1],reverse=True)[:10]
        word_top = dict(word_top)
        # plt.bar(x=word_top.keys(),height=word_top.values())
        # plt.ylim((0,350))

        myframe = DataFrame(data=word_top.values(),index=word_top.keys())
        print(myframe.T)
        myframe = myframe.T
        myframe.rename(index={0:'빈도수'},inplace=True)
        myframe.plot(kind='bar')
        plt.ylim((0, 350))
        filename = 'data/tojiText_bar.png'
        plt.savefig(filename)


    # end class makeBarChart
# end class Visualization:
# 명사 추출하기
filename = 'data/tojiText.txt'
okt = Okt()
ko_con_text = open(filename,'rt',encoding='utf-8').read()
token_ko = okt.nouns(ko_con_text)

# 불용서 사전 불러오기
stop_word_file = 'data/stopword.txt'
stop_file = open(stop_word_file,'rt',encoding='utf-8')
stop_words = [ word.strip() for word in stop_file.readlines()]
# print(stop_words)

token_ko = [ each_word for each_word in token_ko if each_word not in stop_words]

ko = nltk.Text(tokens=token_ko)
data = ko.vocab().most_common(500) # FreqDist
wordlist = list() # 튜플(단어,빈도수)를 저장하는 리스트

# 빈도수가 60이상이고, 단어의 길이가 2이상인 항목들만 간추리기
for word, count in data:
    if count >= 60 and len(word) >= 2:
        wordlist.append((word,count))

print(wordlist)

visual = Visualization(wordlist)
visual.makeWordCloud()
visual.makeBarChart()
plt.show()