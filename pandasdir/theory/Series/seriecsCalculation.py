from pandas import Series

mylist1 = [30,40,50,60]
myindex1 = ['강호동','유재석','김재동','신동엽']
mylist2 = [20,40,60,70]
myindex2 = ['강호동','유재석','김재동','이수근']

myseries1 = Series(data=mylist1, index=myindex1)
myseries2 = Series(data=mylist2, index=myindex2)

print(myseries1)
print('-'*20)
print(myseries2)
print('-'*20)
print(myseries1 + 5)
print('-'*20)
print(myseries1.add(5))
print('-'*20)
print(myseries1 * 10)
print('-'*20)
print(myseries1 >= 40) # bool
print('-'*20)

# numpy에서는 np.nan 이 있음
# NaN : 데이터 누락됨을 표시...
print(myseries1 + myseries2)
print('-'*20)
print(myseries1.add(myseries2))
print('-'*20)
print(myseries1.add(myseries2, fill_value=0))
print('-'*20)
print('-'*20)
print('-'*20)
print('-'*20)
print('-'*20)