import re

mylist = ['cat','ct','caat']
# 'c'와 't'사이에 a가 0번 이상
regex = 'ca*t'
# 'c'와 't'사이에 a가 0번 이상
regex = 'ca+t'
# 'c'와 't'사이에 a가 0~1회
regex = 'ca?t'
pattern = re.compile(regex)

for item in mylist:
    if pattern.match(item):
        print('적합',item)
    else:
        print('부적합',item)