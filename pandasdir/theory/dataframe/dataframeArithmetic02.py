from pandas import DataFrame, Series
import numpy as np

myindex = ['강감찬','김유신','이순신','광해군']
mylist = [50, 60, 40, 80]
myseries = Series(data=mylist, index=myindex)
print(myseries)
print('-'*30)

# 재색인 -> 인덱스를 조정하거나 재정의 reindex
newindex = ['강감찬','김유신','이순신','대원군','연산군']
result = myseries.reindex(index=newindex, fill_value=0)
print(result)
print('-'*30)

mylist = ['blue','purple','yellow']
myindex = [0,3,6]
myseries = Series(data=mylist, index=myindex)
# print(myseries)
print('-'*30)

result = myseries.reindex(index=range(6),method='ffill')
# print(result)
# result = myseries.reindex(index=range(6),method='bfill')
# print(result)
# result = myseries.reindex(index=range(6),method='nearest')
# print(result)

# 색인 지우기
newdata = result.drop([2])
print(newdata)
print('-'*20)

myindex = ['강감찬','김유신','이순신']
mylist = [50,60,40,80,30,50,80,40,60]
mycolumns = ['서울','부산','광주']
mydata = np.reshape(np.array(mylist),(3,3))

myframe = DataFrame(data=mydata, index=myindex,
                    columns=mycolumns)
print(myframe)
print('-'*30)

newindex = ['강감찬','김유신','이순신','광해군']
result = myframe.reindex(index=newindex,fill_value=0)
print(result)
print('-'*30)

newcolumns = ['서울','부산','광주','울산']
result = myframe.reindex(columns=newcolumns,fill_value=40)
print(result)

# newframe = result.drop(['김유신'], axis=0)
newframe = result.drop(['김유신'], axis='index')
print(newframe)
print('-'*30)

# myframe에 '부산','울산'이라는 컬럼을 제거해 보세요
# result = result.drop(['부산','울산'],axis=1)
result = result.drop(['부산','울산'],'columns')
print(result)