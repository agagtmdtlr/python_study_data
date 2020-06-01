from pandas import DataFrame, Series

# Series 생성
mylist = [40, 20, 30, 60]
myindex = ['강감찬', '이순신', '홍길동', '서태지']
myseries = Series(data=mylist, index=myindex)
print(myseries)
print('-'*20)

# index를 통한 정렬
myseries = myseries.sort_index(ascending=False) # ascending = True: 오름차순 False: 내림차순
print(myseries)
print('-'*20)

myseries = myseries.sort_values(ascending=False)
print(myseries)