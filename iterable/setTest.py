# set() 함수를 사용합니다.
# union,intersection,difference 함수 제공
# 중복 x, 순서 x

mylist = [1]*3+[2]*2+[3]*3+[4]*2+[5]
# print(mylist)
myset = set(mylist)
# print(myset)
#
# newlist = list(myset)
# print(newlist)
#
# myset.add(6)
# print(myset)
#
# myset.update([7,8,9])
# print(myset)
#
# myset.remove(9)
# print(myset)

set1 = set('hello')
print(set1)

set3 =  set(range(1,5))
set4 =  set(range(3,7))

set5 = set3.intersection(set4)
print(set5)

set6 = set3.union(set4)
print(set6)

set7 = set3.difference(set4)
print(set7)
set7 = set4.difference(set3)
print(set7)

