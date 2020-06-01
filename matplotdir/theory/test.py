import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Malgun Gothic')


myframe = pd.read_csv('data/somedata2.csv',encoding='utf-8')
myframe= myframe.melt(id_vars='gender',value_vars=['kor','eng','math'])
print(myframe)

mygrouping = myframe.groupby(['gender','variable'])['value']
mydata = mygrouping.mean().unstack(0)
mydata.plot(kind='line',marker='o')

plt.show()