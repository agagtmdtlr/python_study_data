import random
import sys

# for idx in range(100):
    # random.seed(20) # random 함수의 seed를 배정한다.
    # print(random.random()) # 0 <= 값 < 1.0
    # print(random.randint(1,10)) # 하한값 <= 값 <= 상한값
    # print(random.randrange(5,10,2),end=' , ') # 하한값 <= 값 < 상한값

mylist = [10,30,50,20,60]
print(random.choice(mylist))

random.shuffle(mylist)
print(mylist)