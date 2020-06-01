import re

mylist = ['a1.txt','a12.txt','a123.txt','a1234.txt']

# 'a'와 '.txt' 사이에 숫자가 최소 3개이상인 항목들
# dot(.)은 모든 문자를 의미 / [.]는 '.'문자를 의미하다.
regex = '^a\d{3,}[.]txt$'
pattern = re.compile(regex)

for item in mylist:
    if pattern.match(item):
        print(item,' 적합')
    else:
        print(item,' 부적합')