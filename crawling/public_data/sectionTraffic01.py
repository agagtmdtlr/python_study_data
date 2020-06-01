import pandas as pd
import matplotlib.pyplot as plt

filename = 'data/sectionTraffic.csv'
myframe = pd.read_csv(filename,encoding='utf-8')
print(myframe)

plt.rc('font',family='Malgun Gothic')

print('구간별 1~3월 각 월별 평균')
# FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
mygrouping = myframe.groupby(by=['구간'])['1월','2월','3월']
result = mygrouping.mean()
print(result)

newdata = result.loc[result['1월']>=55000]
print(newdata)

newdata.index.name = '운행 구간'
newdata.columns.name = '월별'

newdata.plot(kind='barh',rot=0,title='구간별 월별 구간 교통량',legend=True)

filename = 'data/sectionTraffic01.png'
plt.savefig(filename)
print(filename+'파일 저장 완료')
##########################################################################
plt.figure()

print('차종별 1월의 평균')
mygrouping = myframe.groupby(['차종'])['1월']
result = mygrouping.mean()

result.plot(kind='pie', title ='차종별 1월의 평균',legend=True,autopct='%1.2f%%')

filename = 'data/sectionTraffic02.png'
plt.savefig(filename)
print(filename+'파일 저장 완료')
##################################################################
plt.figure()

col_mapping = {'1월':'January','2월':'February','3월':'March','4월':'April','5월':'May','6월':'June'}
print(myframe.columns)
mycolumn = ['구간','차종','1월', '2월', '3월', '4월', '5월', '6월']

gugan = '서남원~구례화엄'
newframe = myframe[myframe['구간']==gugan]

newframe = newframe.reindex(columns=mycolumn)
newframe = newframe.rename(columns=col_mapping)
print(newframe.head())

newframe = newframe.set_index(['차종'])
mytitle = f'구간 [{gugan}]의 교통량'
myalpha = 0.7

newframe.plot(kind='bar',rot=0,title=mytitle,alpha=myalpha)

filename = 'data/sectionTraffic03.png'
plt.savefig(filename)
print(filename+'파일 저장 완료')
##########################################################################
plt.figure()

middleSizeCar = myframe[myframe['차종']=='중형차']
myconcern = [str(idx)+'월' for idx in range(1,13)]

mygrouping = middleSizeCar.groupby(['차종'])[myconcern]
newframe = mygrouping.sum().T
print(newframe)

quarter01 = sum(newframe.iloc[0:3,0])
quarter02 = sum(newframe.iloc[3:6,0])
quarter03 = sum(newframe.iloc[6:9,0])
quarter04 = sum(newframe.iloc[9:13,0])

from pandas import Series

myindex = [str(idx)+'사분기' for idx in range(1,5)]
myseries = Series([quarter01,quarter02,quarter03,quarter04],index=myindex)
myseries.name = '중형차 4분기 데이터 현황'
myseries.plot(kind='pie',title='중형차 4분기 데이터 현황',autopct='%1.2f%%',legend=True)

filename = 'data/sectionTraffic04.png'
plt.savefig(filename)
print(filename+'파일 저장 완료')