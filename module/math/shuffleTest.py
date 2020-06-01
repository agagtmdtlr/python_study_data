import random

def shuffleit(lists):
    random.shuffle(lists)
    return lists

mylist = ['이순신', '김유신', '강감찬', '안중근', '김홍도', '권율', '유관순', '조마리아', '신사임당', '황진이','박승식']
mylist = shuffleit(mylist)
for i in range(0,len(mylist),2):
    print(mylist[i:i+2])
