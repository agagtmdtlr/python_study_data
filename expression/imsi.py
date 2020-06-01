import re

with open(file='reg_mem.txt',mode='r',encoding='utf-8') as file:
    lists = [ line.strip().split(',') for line in file.readlines()]

regex1 = '-(\d)'
regex2 = '(\d{4})([년|\-|/|]?)(\d{1,2})([월|\-|/|]?)(\d{1,2})([일|]?)$'
pattern1 = re.compile(regex1)
pattern2 = re.compile(regex2)
newlist = []
for item in lists:

    gnum = int(pattern1.search(item[2]).group().replace('-',''))
    if gnum in (1,3):
        gender = '남자'
    else:
        gender = '여자'
    result = pattern2.search(item[3])
    print(result.group(1))
    print(result.group(3))
    print(result.group(5))
    dates = result.group(1)+'/'+\
            result.group(3).zfill(2)+'/'+\
            result.group(5).zfill(2)
    newlist.append([item[0],item[1],gender,dates])

with open(file='result11.txt',mode='w',encoding='utf-8') as file:
    for item in newlist:
        file.write(','.join(item)+'\n')