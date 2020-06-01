import re

mylist = ['abc1234','dabc4567']

regex = '[a-c]+'
pattern = re.compile(regex)

print('match')
for item in mylist:
    if pattern.match(item):
        print('적합',item)
    else:
        print('부적합',item)

print('search')
for item in mylist:
    if pattern.search(item):
        print('적합',item)
    else:
        print('부적합',item)