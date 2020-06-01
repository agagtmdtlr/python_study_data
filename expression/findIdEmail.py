import re

# 다음 리스트와 정규 표현식을 이용하여 아이디와 메일 주소를 추출하세요.
mylist = ['abc@naver.com', 'aaaa@daum.net']
regex = '(?P<id>[a-z]+)(@)(?P<email>.+)'
pattern = re.compile(regex)
item = pattern.search(mylist[0])
item2 = pattern.findall(mylist[0])
print(item.group('id'))
print(item.group(1),item.group(2),item.group(3))
print(item2)

for i in mylist:
    item = pattern.search(i)
    print(i)
    print('id :',item.group('id'))
    print('email :',item.group('email'))