import re
mylist = ['ab1234','ab123','cd456','ef789','abc12']

regex = '^[a-z]{2}\d{3}$'

pattern = re.compile(regex)
print(pattern.match(mylist[1]))
for item in mylist:
    if pattern.match(item):
        print('문자열 ',item,'은 조건에 적합합니다.')
    else:
        print('문자열 ', item, '은 조건에 부합합니다.')