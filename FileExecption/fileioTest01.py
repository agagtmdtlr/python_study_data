import random

mylist = ['강감찬','이순신','신사임당','윤봉길']

random.shuffle(mylist)
try:
    for i,name in enumerate(mylist):
        no = i+1
        filename = name + str(no).zfill(2) + '.txt'
        with open(filename,'w',encoding='utf-8') as file:
            data = (name+'\n')*no
            file.write(data)
except Exception as err:
    print(err)