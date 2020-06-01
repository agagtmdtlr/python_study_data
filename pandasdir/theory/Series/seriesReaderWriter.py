from pandas import Series

myindex = ['서울','부산','관주','대구','울산','목포','여주']
mylist = [50,60,40,80,70,30,20]
myseries = Series(data=mylist, index=myindex)
print(myseries)

print(myseries[['대구']],type(myseries[['대구']]))
print(myseries['대구'],type(myseries['대구']))

# 콜론은 연속적, 콤마는 이산된 데이터
print(myseries['대구':'목포'])
print(myseries[['대구','목포']])

print(myseries[[2]])
print(myseries[0:5:2])

print(myseries['부산':'여주':2])
print(myseries[1:6:2])

myseries[2:5] = 33
print(myseries)

myseries[['대구','서울']] = 55
myseries[::2] = 80
print(myseries)
