import numpy as np
import pandas as pd
import random
from pandas import DataFrame

mylist = [ 10 * onedata for onedata in range(1,26)]
mydata = np.reshape(np.array(mylist),newshape=(5,5))

myindex = ['박승식','홍길동','김정호','강수지','심형래']
mycolumns = ['서울','부산','광주','목포','경주']
myframe = DataFrame(data=mydata, index=myindex,columns=mycolumns)
print(myframe)

# attribue
# iloc : 인덱스 기반으로 데이터 추출
# index location
result = myframe.iloc[1] # return Series
print(result)
print('-'*20)

result = myframe.iloc[[1,3]] # return Dataframe
print(result)
print('-'*20)

result = myframe.iloc[0::2]
print(result)

# loc : 라벨을 기반으로 데이터 추출
result = myframe.loc['홍길동'] # return Series
print(result)
print('-'*20)

result = myframe.loc[['홍길동']] # return Series
print(result)
print('-'*20)

result = myframe.loc[['박승식','김정호']]
print(result)
print('-'*20)
print(myframe.index)

# 데이터 프레임에서 복원추출로
# 임의의 사람 3명에 대한 정보를 추출해 보세요
mytarget = np.random.choice(myframe.index,3)
print(mytarget)
result = myframe.loc[mytarget]
print(result)

result = myframe.loc[['박승식','김정호'],['광주','목포']] # loc[[행],[열]] return dataframe
print(result)
result = myframe.loc[['박승식','김정호'],'광주'] # scarlar or Series
print(result)

result = myframe.loc['박승식':'김정호','광주':'경주']
print(result)

result = myframe.loc[[False,True,True,False,True]]
print(result)

# 부산 실적이 100이하인것들
print(myframe['부산'] <= 100) # return Seriec dtype bool
result = myframe.loc[myframe['부산'] <= 100] # so you can't use '논리연산자'
print(result)

print(myframe.loc[myframe['목포'] == 140])

# 부산 >= 70, 목포 >= 140
cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140
print(cond1,cond2)

df = DataFrame(data=[cond1,cond2])
print(df)
print(df.all()) # 논리 곱 and
print(df.any()) # 논리 합 or

print(myframe.loc[df.all()])
print(myframe.loc[df.any()])

# result = myframe.loc[lambda df : df['광주'] >= 130]
# print(result)
#
# myframe.loc[['박승식','김정호'],['부산']] = 550
# print(myframe)
#
# # 홍길동 부터 강수지 까지 경주 실정 80변경
# myframe.loc['홍길동':'강수지','경주'] = 80 # ['홍길동':'강수지',['경주']]
# print(myframe)
# # 심형래의 모든 실적을 50으로 변경
# myframe.loc['심형래'] = 50 # [['심형래'],:]
# print(myframe)
#
# # 모든 사람의 광주컬럼을 60으로 병
# myframe.loc[:,'광주'] = 60
# print(myframe)