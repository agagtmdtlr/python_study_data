#상자 수염 그래프

import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')

filename = 'data/tips.csv'
myframe = pd.read_csv(filename,encoding='utf-8')

# time : 점심, 저녁
print(myframe['time'].unique())

# total_bill : 총 지불 금액
frame01 = myframe.loc[myframe['time']=='Dinner','total_bill']
frame01.index.name = 'Dinner'

frame02 = myframe.loc[myframe['time']=='Lunch','total_bill']
frame02.index.name = 'Lunch'

print(frame01.max(),frame01.mean())

print(frame02.max(),frame02.mean())

totalframe = pd.concat([frame01,frame02], axis=1,ignore_index=True)
totalframe.columns = ['Dinner','Lunch']
print(totalframe)

totalframe.plot(kind='box')

plt.xlabel('지불시간')
plt.ylabel('총 지금액')
plt.title('상자 수염 그래프')

# filename = 'concat_data/boxplot01.png'
# plt.savefig(filename, dpi=400, bbox_inches='tight')
# print(filename+'파일 저장 완료')
#
# plt.show()