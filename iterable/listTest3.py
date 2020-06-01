# 중첩 리스트
saram01 = ['hong','홍길동',20,'용산']
saram02 = ['kim','김철수',30,'마포']
saram03 = ['kang','강남',40,'강남']

mylist = [] # empty list
mylist.extend((saram01,saram02,saram03))

print(mylist)

mylist[2][1] = '강호동'; print(mylist[2][1])
total = mylist[0][2]+mylist[1][2]+mylist[2][2]
mylen = len(mylist)
print('평균 나이 :',total/mylen)

newlist = list((saram01[1],saram02[1],saram03[1]))
print('$'.join(newlist))
