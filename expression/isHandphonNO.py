import re

mylist = ['010-1111-2222','aa010-1111-2222가가','01011112222']

regex = '^\d{3}-\d{4}-\d{4}$'
pattern = re.compile(regex)

for item in mylist:
    if pattern.match(item):
        print('적합',item)
    else:
        print('부적합',item)