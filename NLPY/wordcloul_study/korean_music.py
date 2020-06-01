import nltk # national language tool-kit
import numpy as np
import matplotlib.pyplot as plt

from konlpy.tag import Okt
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from PIL import Image


filename = 'data/애국가(가사).txt'
# filename = 'concat_data/문재인대통령신년사.txt'
ko_con_text = open(filename,'rt',encoding='utf-8').read()

okt = Okt()

token_ko = okt.nouns(ko_con_text)
print(type(token_ko))
print(token_ko)
print(len(token_ko))

# 이것도 파일로 만들어 두면 좋을 듯....
stop_words = ['제','월','일','조','그','아','철']

# 불용어는 분석 목록에서 제외합니다.
token_ko = [ each_word for each_word in token_ko if each_word not in stop_words]

ko = nltk.Text(tokens=token_ko)
print(type(ko)) # Text
print(type(ko.vocab())) # FreqDict (빈도수를 저장하고 있는 사전)
print(ko.vocab())
print(ko.vocab().most_common(50)) # 리스트
print(len(ko.vocab().most_common(50)))

data = ko.vocab().most_common(500)
tmp_dict = dict(data)
# dict(iterable) -> new
# dictionary
# initialized as if via:
#     d = {}
#     for k, v in iterable:
#         d[k] = v
alice_color_file = 'data/alice_color.png'

alice_color_mask = np.array(Image.open(alice_color_file))

wordcloud = WordCloud(font_path='malgun.ttf',mask=alice_color_mask, background_color='white')
wordcloud = wordcloud.generate_from_frequencies(tmp_dict)

image_color = ImageColorGenerator(alice_color_mask)

newwc = wordcloud.recolor(color_func=image_color,random_state=100)

plt.imshow(newwc,interpolation='bilinear')
plt.axis('off')

filename = 'national.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다.')

plt.show()
print('finished')