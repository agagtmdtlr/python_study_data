from pandas import Series

mylist = [10,40,30,20]
myseries = Series(data=mylist,
                  index=['강감찬','이순신','김유신','광해군'])
print(type(myseries))

myseries.index.name = '점수'

myseries.name = '학생들 시험'

print(myseries)

print(myseries.index)
print(myseries.values)
for idx in myseries.index:
    print(f'색인 : {idx},값 : {myseries[idx]}')