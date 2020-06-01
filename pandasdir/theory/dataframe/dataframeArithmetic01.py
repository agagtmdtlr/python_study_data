from pandas import DataFrame, Series
import numpy as np

myindex = ['강호동','유재석','신동엽']
mylist = [30,40,50]
myseries = Series(data=mylist, index=myindex)
print(myseries)
print('-'*20)

myindex = ['강호동','유재석','이수근']
mycolumn = ['서울','부산','경주']
mylist = [10*one for one in range(1,10)]
mydata = np.reshape(np.array(mylist),(3,3))
myframe = DataFrame(data=mydata,index=myindex,columns=mycolumn)
print(myframe)
print('-'*20)


#데이터 프레임, 시리즈 연산
result = myframe.add(myseries,axis=0)
result = myseries.add(myframe,axis=0,fill_value=0)
print(result)

myindex2 = ['강호동','유재석','김병만']
mycolumn2 = ['서울','부산','대구']
mylist2 = [5*one for one in range(1,10)]
mydata2 = np.reshape(np.array(mylist2),(3,3))
myframe2 = DataFrame(data=mydata2,index=myindex2,columns=mycolumn2)
print(myframe2)
print('-'*20)

# 데이터 프레임, 데이터프레임 연산
result = myframe.add(myframe2,fill_value=0)
print(result)
print('-'*20)
result.loc[['김병만'],['경주']] = 0
result.loc[['이수근'],['대구']] = 0
print(result)
print('-'*20)