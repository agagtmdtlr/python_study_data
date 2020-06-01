import numpy as np
import matplotlib.pyplot as plt

from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
from wordcloud import WordCloud
from PIL import Image


alice = Image.open('data/alice_color.png')
mask = np.array(alice)
text = open('data/steve.txt','rt',encoding='utf-8').read()
color = ImageColorGenerator(mask)
stopw = set(STOPWORDS)
stopw.add('life')
stopw.update(['years','month','year'])
wc = WordCloud(stopwords=stopw,include_numbers=True,max_words=20,
               mask=mask,random_state=300,color_func=color).generate(text)

plt.imshow(wc)
plt.axis('off')
plt.show()

