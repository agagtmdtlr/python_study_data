import numpy as np
from pandas import DataFrame, Series

# Dataframe 생성
mylist = [40, 20, 30, 60,50,70,80,10]
myindex = ['강감찬', '이순신']
mycolumns = ['one','two','three','four']
mydata = np.array(mylist).reshape(2,4)
myframe = DataFrame(data=mydata, index=myindex, columns=mycolumns)
# print(myframe)
# print('-'*20)
#
# myframe = myframe.sort_index(ascending=False)
# print(myframe)
#
# print(myframe.sort_index(axis=0)) # row
# print(myframe.sort_index(axis=1)) # column


mydict = {'국어':[40,70,30,20],'영어':[50,20,50,20]}
myindex = ['강호동', '유재석', '신동엽', '이수근']
myframe = DataFrame(data=mydict, index=myindex)
print(myframe)
print('-'*30)
#
# print(myframe.sort_values(by=['국어'], ascending=[False]))
# print('-'*30)
#
# # 영어 점수가 낮은 사람부터 오름차 정렬
# print(myframe.sort_values(by=['영어'], ascending=[True]))
#
# # 영어 점수 오름차, 국어 점수 내림차 정렬
# print(myframe.sort_values(by=['영어','국어'], ascending=[True,False]))

# Ranking 에 쓰는 함수
myseries = Series(data=[0,1,1,2], index=['강호동', '유재석', '신동엽', '이수근'])
#
# print(myseries.rank())
# print('-'*30)
#
# # 공동 rank 처리 방식
# print(myseries.rank(method='first'))
# print('-'*30)
# print(myseries.rank(method='min'))
# print('-'*30)
# print(myseries.rank(method='max'))
# print('-'*30)
# print(myseries.rank(method='min',ascending=False))

print(myframe.rank())
print('-'*20)
# row
print(myframe.rank(axis=0))
print('-'*20)
# col
print(myframe.rank(axis=1))
print('-'*20)

