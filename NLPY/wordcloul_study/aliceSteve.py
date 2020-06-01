from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator

image_file = 'data/alice.png'
img_file = Image.open(image_file)
print(type(img_file)) #<class 'PIL.PngImagePlugin.PngImageFile'>

alice_mask = np.array(img_file)
print(alice_mask)
print(alice_mask.shape)

plt.figure(figsize=(8,8))
plt.imshow(alice_mask,interpolation='bilinear')
plt.axis('off')

filename = 'data/graph01.png'
plt.savefig(filename)

# stopword 불용어 사전 (분석에 쓸모없는 것)
mystopwords = set(STOPWORDS)
mystopwords.update(['hahaha','hohoho'])
print(len(mystopwords))


wc = WordCloud(background_color='white', max_words=2000,
               mask=alice_mask,stopwords=mystopwords)

stevefile = 'concat_data/steve.txt'
text = open(stevefile,'rt',encoding='utf-8')
text = text.read()

wc = wc.generate(text)
# print(wc.words_)

plt.figure(figsize=(8,8))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')

filename = 'data/graph02.png'
plt.savefig(filename)

alice_color_file = 'data/alice_color.png'
alice_color_mask = np.array(Image.open(alice_color_file))

wc = WordCloud(background_color='white', max_words=2000,
               mask=alice_color_mask,stopwords=mystopwords,
               max_font_size=40, random_state=43)

wc = wc.generate(text)

plt.figure(figsize=(8,8))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')

filename = 'data/graph03.png'
plt.savefig(filename)

plt.figure(figsize=(8,8))
plt.imshow(alice_color_mask,interpolation='bilinear')
plt.axis('off')

filename = 'data/graph04.png'
plt.savefig(filename)

image_color = ImageColorGenerator(alice_color_mask)
print(type(image_color))

newwc = wc.recolor(color_func=image_color,random_state=42)

plt.figure(figsize=(8,8))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')

filename = 'data/graph05.png'
plt.savefig(filename)

plt.show()
