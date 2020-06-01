import re

mystr = 'abcd 1234 abAB'
regex = '[a-d]+'
pattern = re.compile(regex)

mylist = pattern.findall(mystr)
print(type(mylist),mylist)

myiter = pattern.finditer(mystr)
print(type(myiter))
print(myiter)

for abcd in myiter:
    # print(type(abcd))
    print(abcd)
    print('start :',abcd.start())
    print('end() :',abcd.end())
    print('span() :',abcd.span())
    print('문자열 :',mystr[abcd.start():abcd.end()])
    print('문자열 :', abcd.group())