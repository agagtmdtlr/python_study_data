import re
lists = []
with open(file='id.txt',mode='r',encoding='utf-8') as file:
    lists = [i.strip() for i in file.readlines()]

regex = '\(\w+\)'
pattern = re.compile(regex)

for item in lists:
    mystr = pattern.search(item)
    if mystr :
        print('id : ',mystr.group().strip("()"))
    else:
        print('no id')
