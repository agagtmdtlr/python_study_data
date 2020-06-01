# 조배정 문제
import numpy as np

filename = 'member.txt'
with open(file=filename,mode='r',encoding='utf-8') as myfile :
    data = myfile.readlines()
print(data)

result = np.random.permutation(len(data))
print(result)

members = []
for mem in data:
    members.append( mem.strip())

print(members)

import time

for idx in range(len(result)):
    num = result[idx]
    print(members[num], end =' ')

    if (idx % 4 == 3):
        print()
        print('-'*20)
    time.sleep(1)
import random
random.shuffle(members)
print(members)