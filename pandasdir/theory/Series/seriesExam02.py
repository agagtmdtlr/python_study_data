from pandas import Series
import pandas
mylist = ['라일락','코스모스','코스모스','백일홍','코스모스',
          '코스모스','들장미','들장미','라일락','라일락']

myseries = Series(mylist)
print(myseries)

myunique = myseries.unique() # return ndarray
print(myunique)

print(myseries.value_counts())  # 빈도수 구하기

mask = myseries.isin(['들장미','라일락'])
print(mask)
print(myseries[mask])

print(type(mask))
print('-'*20)


