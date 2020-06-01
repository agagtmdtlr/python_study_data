mylist = [10,5,30,20]
print('# 원본 :',mylist)

mylist.sort()
print('# 오름차 정렬 :',mylist)

mylist.sort(reverse=True)
print('# 오름차 정렬 :',mylist)

print('# 아스키 코드 확인')
print('ord(\'A\') :',ord('A'))
print('ord(\'a\') :',ord('a'))

newlist = ['A','b','C','d']
newlist.sort()
print('# 오름차 정렬 :',newlist)

newlist.sort(key=str.lower)
print('# 소문자로 변경 후 정렬 :',newlist)

newlist.sort(key=str.lower,reverse=True)
print('# 소문자로 변경 후 정렬 :',newlist)

smallcahr = [i.lower() for i in newlist]
print('# 모두 소문자화 :',smallcahr)