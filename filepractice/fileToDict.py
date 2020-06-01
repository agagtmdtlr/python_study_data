with open(file='data/mem.txt',mode='r',encoding='utf-8') as file:
    lines = [i.strip().split(',') for i in file.readlines()]
    dicts = { i[0] : int(i[1]) for i in lines}
    dicts = sorted(dicts.items(),key=lambda x : x[1])
    for i in dicts:
        print(i[0],',',i[1])