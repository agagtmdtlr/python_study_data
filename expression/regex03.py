import re

# .은 줄바꿈 문자를 제외한 모든 글자를 의미합니다.
mystr = 'a\nb'
regex = 'a.b'

print('줄바꿈 문자 무시됨')
pattern = re.compile(regex)
mymatch = pattern.match(mystr)
print(mymatch)
print('-'*20)

print('줄바꿈 문자 포함됨')
pattern = re.compile(regex, re.RegexFlag.DOTALL)
mymatch = pattern.match(mystr)
print(mymatch)
print('-'*20)

print('대소문자 구분하기')
print('대소문자를 구분합니다.')
mystr = 'PYTHON'
regex = '[a-z]+'
pattern = re.compile(regex)
mymatch = pattern.match(mystr)
print(mymatch)
print('-'*20)

print('대소문자를 구분하지 않습니다.')
mystr = 'PYTHON'
regex = '[a-z]+'
pattern = re.compile(regex, re.RegexFlag.IGNORECASE)
mymatch = pattern.match(mystr)
print(mymatch)
print('-'*20)

mystr = '''python one
python two hello python three
you need python
python four hahaha'''

# \s : white character
# 맨 앞에 python가 나오고, 뒤에 white charater 1글자
# 나온다음 문자나 숫자가 최소 1개 이상 나와야 합니다.
# \w : 문자 and 숫자

regex = '^python\s\w+'
print('멀티라인 적용 안됨')
pattern = re.compile(regex)
mymatch = pattern.match(mystr)
print(mymatch)
print('-'*20)

print('멀티라인 적용 됨')
pattern = re.compile(regex, re.RegexFlag.MULTILINE)
mymatch = pattern.findall(mystr)
print(mymatch)
print('-'*20)