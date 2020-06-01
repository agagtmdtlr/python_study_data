tuple1 = (1,2,3)
print(tuple1)

tuple1 = tuple1 + (4,) # 튜플은 튜플끼리
# tuuple1 = tuple1 + tuple([4])
print(tuple1)

tuple2 = 1,2,3 #단순 나열은 tuple로 전환
print(tuple2)

mylist = [1,2,3,4]
tuple3 = tuple(mylist) # iterable 자료형 튜플로 전환 가능
print(tuple3)

tuple4 = (1,2,3)
tuple5 = (4,5,6)

tuple6 = tuple4 + tuple5
print(tuple6)

tuple7 = tuple3*3
print(tuple7)

a,b = 10,20
a,b = b,a
print('a',a,'b',b)

# 튜플 인덱싱은 숫자 변수
# 튜플 슬라이싱은 튜플 변수
tuple8 = 1,2,3,4,5,6
print(tuple8[2])
print(tuple8[1:3])
print(tuple8[3:])

#튜플은 값 변경이 안된다.
# tuple8[0] = 100

# 원소 100개짜리 튜플 mytuple 만들기
# 10이 30, 20이 30, 30이 30, 40이 10
mytuple = (10,)*30+(20,)*30+(30,)*30+(40,)*10
print(mytuple,len(mytuple),sep='\n')