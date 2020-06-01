import random

mydict = dict()
for i in range(100):
    num = random.randint(1,10)
    if mydict.get(num) is not None:
        mydict[num] = mydict.get(num)+1
    else:
        mydict[num] = 1
for i in range(1,11):
    print(f'{i} : {mydict[i]}',end='\n')