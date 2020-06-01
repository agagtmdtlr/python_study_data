import re

mystr = '1234 abc가나다AB_555_6'

# 총합 = 12 + 34 + 55 = 101
regex = '\d{2}'
pattern = re.compile(regex)

total = 0

mylist = pattern.findall(mystr)
for item in mylist:
    print(item)
    total += int(item)
print(total)

total = 0
myiter = pattern.finditer(mystr)
for item in myiter:
    print(item.group())
    total += int(item.group())
print(total)