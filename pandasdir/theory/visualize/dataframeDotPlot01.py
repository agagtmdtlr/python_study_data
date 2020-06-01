import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')

filename = 'data/mpg.csv'
myframe = pd.read_csv(filename, encoding='utf-8')
# print(myframe.head())
# print(myframe.info())

# x 축 : displ(엔진 크기), y 축 : hwy(고속도로 주행 마일수)
# drv : 구동방식으로 색상 구분
labels = myframe['drv'].unique()
# print(labels) #['f' '4' 'r']
mycolor = ['r','g','b']

cnt = 0
for finditem in labels:
    xdata = myframe.loc[myframe['drv']==finditem,'displ']
    ydata = myframe.loc[myframe['drv']==finditem,'hwy']
    plt.plot(xdata, ydata, color=mycolor[cnt], linestyle='None', marker='o', label=finditem)
    cnt += 1

plt.legend()
plt.xlabel('엔진 크기')
plt.ylabel('주행 마일수')
plt.title('산점도')

filename = 'data/dotplot.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+'파일 저장 완료')

plt.show()