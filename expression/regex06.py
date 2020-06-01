import re

with open(file='reg_mem.txt',mode='r',encoding='utf-8') as file:
    lists = [ line.strip().split(',') for line in file.readlines()]

regex1 = '-(\d)'
regex2 = '(\d{4}[년\-/]?)(\d{1,2}[월\-/]?)(\d{2}[일]?)'
result = []
for item in lists:
    pattern1 = re.compile(regex1)
    print()
    gnum = int(pattern1.search(item[2]).group().replace('-',''))
    if gnum in (1,3):
        gender = '남자'
    else:
        gender = '여자'
    pattern2 = re.compile(regex2)
    # print(pattern2.search(item[3]).group(0))
    print(pattern2.search(item[3]).group(1))
    print(pattern2.search(item[3]).group(2))
    print(pattern2.search(item[3]).group(3))