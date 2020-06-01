import numpy as np
from pandas import DataFrame

mydata = [[10.0,np.nan,20.0],\
          [20.0,30.0,40.0],\
          [np.nan,np.nan,np.nan],\
          [40.0,50.0,30.0]]

myindex = ['강감찬','김유신','이순신','홍길동']
mycolumn = ['국어','영어','수학']

myframe = DataFrame(mydata,index=myindex,columns=mycolumn)

print(myframe)
print('-'*20)

print(myframe.sum(axis=1)) # 1 : column arrow
print('-'*20)
print(myframe.sum(axis=0)) # 0 : index arrow
print('-'*20)
print(myframe.sum(axis=1,skipna=False))
print('-'*20)
print(myframe.idxmax())
print('-'*20)
print(myframe.cumsum(axis=1))
print('-'*20)
print(myframe.cumprod(axis=1))
print('-'*20)
print(myframe.cummax(axis=1))

# myframe.loc[myframe['국어'].isnull(),'국어'] = 55
# myframe.loc[myframe['영어'].isnull(),'영어'] = 60
# myframe.loc[myframe['수학'].isnull(),'수학'] = 30

# 데이터의 평균으로 nan 값을 채워넣기
myframe.loc[myframe['국어'].isnull(),'국어'] = myframe['국어'].mean(axis=0,skipna=True)
myframe.loc[myframe['영어'].isnull(),'영어'] = myframe['영어'].mean(axis=0,skipna=True)
myframe.loc[myframe['수학'].isnull(),'수학'] = myframe['수학'].mean(axis=0,skipna=True)

print(myframe)
print('-'*20)

# 다양한 통계값 산출
print(myframe.describe())
print('-'*20)
# 인덱스, 칼럼 , 결측치 확인
print(myframe.info())