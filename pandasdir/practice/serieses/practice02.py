from pandas import Series
import numpy.random as nprd
import random as rd

mylist = ['라일락','코스모스','백일홍','들장미']
# print(nprd.randint(4,size=(4,4)))
# print(rd.choice(mylist)) # test

#반복문으로 100번 실행하여 매번 mylist에서
# 요소 1개를 추출하여 리스트에 저장합니다.
# 해당 리스트를 이용하여 Series를 만드시오.
# sdata = [rd.choice(mylist) for i in range(100)]
sdata = nprd.choice(mylist,100)
myseries = Series(data=sdata,name='flower')
print(myseries)

#각각의 꽃에 대한 빈도 수를 구해보세요.
print(myseries.value_counts())

# 값이 '백일홍', '들장미'인 항목들만 필터링 해보세요.
# mask = myseries.isin(['백일홍','들장미'])
# print(myseries[mask])
# print(myseries[mask].value_counts())


# print(myseries[(myseries == '백일홍')|(myseries=='들장미')])
# print(myseries[~myseries.isin(['백일홍','들장미'])])

lists1 = [1,2,3,4,5]
l = lambda x : x in (1,2)
l2 = lambda x : x in ('백일홍','들장미')
print(l(3))
print(l2('백일홍'))


# print(myseries.loc[lambda x : x == '백일홍'])