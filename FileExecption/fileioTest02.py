import random
with open(file='sample02.txt',mode='w',encoding='utf-8') as file:
    for i in range(10):
        x= random.randrange(50,101,5)
        file.write(str(x)+'\n')

with open(file='sample02.txt',mode='r',encoding='utf-8') as file:
    lines = [int(x.strip()) for x in file.readlines()]
    suml = sum(lines)
    print(suml)