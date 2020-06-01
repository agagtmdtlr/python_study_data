import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

filename = 'data/welfare_python.csv'
myframe = pd.read_csv(filename,encoding='utf-8')
print(myframe['religion'].unique())
mygrouping = myframe.groupby(by='religion')['religion']
mydata = mygrouping.count()

mydata.plot(kind='bar',rot=0,color=['r','g'])
# filename = 'concat_data/welfare_05_01.png'
# plt.savefig(filename,dpi=400, bbox_inches='tight')
# plt.figure()
# print(filename + '파일 저장 완료')

mydata.plot(kind='pie',rot=0,startangle=90,
            autopct='%.2f%%')
# filename = 'concat_data/welfare_05_02.png'
# plt.savefig(filename,dpi=400, bbox_inches='tight')
# plt.figure()
# print(filename + '파일 저장 완료')

print(myframe['marriage'].unique())

# myframe.info()
marr = DataFrame({'marriage':[1,3],'marr':['결혼','이혼']})
print(marr)

newframe = pd.merge(myframe,marr,on='marriage',how='outer')
# newframe.info()
mygrouping= newframe.groupby(by='marr')['marr']
mydata = mygrouping.count()
mydata['Nan'] = len(newframe)-sum(mydata)
print(mydata)
mydata.plot(kind='pie',rot=0,autopct='%.2f%%')

# filename = 'concat_data/welfare_05_03.png'
# plt.savefig(filename,dpi=400, bbox_inches='tight')
# plt.figure()
# print(filename + '파일 저장 완료')

##############################################
newframe.info()

newframe.loc[newframe['marriage']==1,'marr2'] ='결혼'
newframe.loc[newframe['marriage']!=1,'marr2'] ='비결혼'

mygrouping = newframe.groupby(by=['marr2','religion'])['marr2']
mydata = mygrouping.count().unstack(0)
print(mydata)

# mydata.plot(kind='bar',rot=0)
# filename = 'welfare_05_04.png'
# plt.savefig(filename,dpi=400, bbox_inches='tight')
# plt.figure()
# print(filename + '파일 저장 완료')
plt.figure()
#####################################
newframe['age'] = 2020 - newframe['birth']+1
cond1 = newframe['age'] >= 10
cond2 = newframe['age'] < 60
condf = DataFrame([cond1,cond2])
result = condf.all()

ageframe = newframe[result].__deepcopy__()
ageframe.info()

ageframe['ageg'] = ageframe['age'].apply(lambda x:str((x//10)*10))+'대'
ageframe['gender'] = ageframe['gender'].apply(lambda x:'남자'if x==1 else'여자')

mygrouping=ageframe.groupby(by=['gender','ageg'])['ageg']
mydata = mygrouping.count().unstack(0)
mydata.plot(kind='bar',rot=0)

# filename = 'welfare_05_05.png'
# plt.savefig(filename,dpi=400, bbox_inches='tight')
# plt.figure()
# print(filename + '파일 저장 완료')
plt.figure()
##############################################

mygrouping=ageframe.groupby(by=['ageg','religion'])['ageg']
mydata = mygrouping.count().unstack(1)
mydata.plot(kind='bar',rot=0)

# filename = 'welfare_05_06.png'
# plt.savefig(filename,dpi=400, bbox_inches='tight')
# plt.figure()
# print(filename + '파일 저장 완료')
plt.figure()
########################################################
mygrouping=ageframe.groupby(by=['ageg','marr2'])['ageg']
mydata = mygrouping.count().unstack(1)
print(mydata)
mydata.loc[['20대','30대']].plot(kind='bar',rot=0)

# filename = 'concat_data/welfare_05_07.png'
# plt.savefig(filename,dpi=400, bbox_inches='tight')
# plt.figure()
# print(filename + '파일 저장 완료')

##############################################
mygrouping=newframe.loc[myframe['income'].notnull(),:].groupby(by='marr2')['income']
mydata = mygrouping.mean()
print(mydata)
mydata.plot(kind='bar',rot=0,color=['r','b'])

# filename = 'concat_data/welfare_05_08.png'
# plt.savefig(filename,dpi=400, bbox_inches='tight')
# plt.figure()
# print(filename + '파일 저장 완료')
