import pandas as pd
import matplotlib.pyplot as plt

filename = 'data/capital_area.csv'

pd.options.display.max_rows = 1000
pd.options.display.max_columns = 1000
myframe = pd.read_table(filename,sep='|')
# print(myframe)

print(myframe.info())

print(myframe.columns)

print(myframe['영업소코드'].unique())
print('-'*20)

mygrouping = myframe.groupby('영업소코드')['총교통량']
chartdata = mygrouping.sum()
print(chartdata)
print('-'*20)

plt.rc('font', family='Malgun Gothic')
chartdata.index.name = 'Total Traffic'
newindex = ['코드('+str(key)+')' for key in chartdata.index]
chartdata.index = newindex
mytitle = '영업소코드 별 교토량의 총합'
chartdata.plot(kind='bar',title=mytitle,figsize=(10,6),legend=True)

filename = 'data/capitalArea01.png'
plt.savefig(filename)
print(filename+'파일 저장 완료')

print('파이썬 내장 함수')
print(max(myframe['1종교통량']))

print('데이터 프레임의 집계 함수')
print(myframe['1종교통량'].max())
print('-'*20)
# plt.show()
#####################################################
plt.figure()
myframe = myframe.set_index('집계일자')

myframe = myframe.loc[['20170201','20170202','20170203']]

mygrouping = myframe.groupby('집계일자')['총교통량']
chartdata = mygrouping.sum()
print(chartdata)
print('-'*20)

chartdata.index.name = 'Total Traffic'
newindex = [ str(idx)[4:6]+'월'+str(idx)[6:8]+'일' for idx in chartdata.index]
print(newindex)
chartdata.index = newindex

mytitle = '영업소코드 별 교통량의 누적합'
chartdata.plot(kind='pie',title=mytitle,figsize=(10,6),legend=True,autopct = '%1.2f%%')

filename = 'data/capitalArea01.png'
plt.savefig(filename)
print(filename+'파일 저장 완료')

plt.show()
###########################################################